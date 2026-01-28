import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
MODEL_PATH = "models/best.pt"
LOG_FILE = "logs/app.log"
