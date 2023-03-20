import os
from dotenv import dotenv_values
from pathlib import Path

base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
dotenv_values(env_file)


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

