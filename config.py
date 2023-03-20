import os
from dotenv import load_dotenv

load_dotenv()
print('sssx', os.environ.get('SECRET_KEY'))

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

