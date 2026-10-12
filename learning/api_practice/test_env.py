import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AI_API_KEY")

print("API_KEY:", api_key)