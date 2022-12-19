import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = 'MyTTA (My Trouble Ticket Assistant'
    PROJECT_VERSION: str = '0.2b'

settings = Settings()