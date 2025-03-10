import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logpath=os.path.join(os.getcwd(),"logs")
os.makedirs(logpath,exist_ok=True)
LOGFILE_PATH=os.path.join(logpath,LOG_FILE)
logging.basicConfig(level=logging.INFO,filename=LOGFILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s")