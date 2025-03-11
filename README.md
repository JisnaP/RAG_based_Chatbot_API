# RAG-Based Chatbot API

This is a **Flask REST API** that implements a **Retrieval-Augmented Generation (RAG) chatbot** using FAISS for vector search and Google Generative AI for generating responses. The API retrieves relevant documents from FAISS and generates accurate answers using a Large Language Model (LLM).

## Features
- Uses **FAISS** for similarity search on stored document embeddings.
- Utilizes **Google Generative AI** for intelligent response generation.
- Implements **Flask-RESTful** for API development.
- Provides structured JSON responses with retrieved document sources.

---

## Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/JisnaP/RAG_based_Chatbot_API.git
cd RAG_based_Chatbot_API
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate  
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## Usage

### 1️⃣ Start the Flask Server
```sh
python app.py
```
This runs the API on `http://localhost:8080` .

### 2️⃣ Send a Request to the API
Use **cURL**, Postman, or a Python request to interact with the chatbot.

#### Example Request (cURL):
```sh
curl -X POST "http://localhost:8080/chat" \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the courses available on brainlox?"}'


---
```
## API Endpoints

### `POST /chat`
- **Request:** JSON with a `query` field.
- **Response:** JSON containing the answer and context sources.
```


## Project Structure
```
chatbot-api/
│── chatbot/
│   ├── data_ingestion.py  # Loads documents into FAISS index
│   ├── embeddings.py      # Handles embeddings using Google Generative AI
│   ├── model.py          # Loads the language model
│── app.py               # Main Flask API
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## Troubleshooting

### 🔹 415 Unsupported Media Type Error
**Cause:** Content-Type is not set to `application/json`.
**Fix:** Ensure the request includes:
```sh
-H "Content-Type: application/json"
```

### 🔹 FAISS Index Not Found
**Cause:** The FAISS index is missing.
**Fix:** Run the data ingestion script to generate the FAISS index:
```sh
python chatbot/data_ingestion.py
```

---

## License
This project is open-source under the **MIT License**.

---

## Author
**Jisna Patharakkal**



