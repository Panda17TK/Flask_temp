import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

try:
    DSN = os.environ.get("DB_NAME")
    USN = os.environ.get("USER_NAME")
    PWD = os.environ.get("PASSWORD")
except:
    print("Error: Could not load environment variables.")
