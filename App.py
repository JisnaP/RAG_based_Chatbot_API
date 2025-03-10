from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from chatbot.data_ingestion import load_data
from chatbot.embeddings import download_gemini_embedding
from chatbot.model import load_model

app = Flask(__name__)
api = Api(app)

# Load FAISS index
documents = load_data()
embeddings = download_gemini_embedding(documents)
vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

llm = load_model()

retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={"k": 3})

system_prompt = (
    "You are an intelligent assistant specializing in answering questions based on provided context. "
    "Carefully read the retrieved docs and provide a concise, accurate response. "
    "If the retrieved docs do not contain the information needed to answer, you MUST respond with 'I don't know.' "
    "Do not attempt to predict or fabricate information. "
    "Keep your response to three sentences or fewer to maintain brevity."
    "\n\n"
    "Context:\n{context}"
)

Human_prompt = "{input}"
prompt = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("human", Human_prompt)
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

class Chatbot(Resource):
    def post(self):
        try:
            user_input = request.json.get("query")
            if not user_input:
                return {"error": "Query not provided"}, 400

            response = rag_chain.invoke({"input": user_input})

            # Extract structured response
            if isinstance(response, dict):
                answer = response.get("answer", "No answer available")
                context = [
                    {
                        "source": doc.metadata.get("source", "Unknown"),
                        "title": doc.metadata.get("title", "Unknown"),
                        "description": doc.metadata.get("description", "No description available"),
                    }
                    for doc in response.get("context", [])
                ]
            else:
                answer = str(response)
                context = []

            return {
                "query": user_input,
                "answer": answer,
                "context_sources": context
            }

        except Exception as e:
            return {"error": str(e)}, 500
    


api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
