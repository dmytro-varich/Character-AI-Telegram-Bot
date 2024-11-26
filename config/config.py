from dotenv import load_dotenv
import os 

load_dotenv()

CHAT = os.getenv("CHAT")
TG_TOKEN = os.getenv("TG_TOKEN")
OWN_ID = int(os.getenv("OWN_ID"))
OWN_ID_2 = int(os.getenv("OWN_ID_2"))
