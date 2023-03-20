import os
from dotenv import load_dotenv

load_dotenv()
print('sssx', os.getenv('SECRET_KEY'))

class Config:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY')

