import os
from dotenv import load_dotenv

load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
invalid_email = "User123"
invalid_password = "9844656332447"