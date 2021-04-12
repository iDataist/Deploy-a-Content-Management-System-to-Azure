import os
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

class Config(object):
    SQL_SERVER = os.getenv('SQL_SERVER') 
    SQL_DATABASE = os.getenv('SQL_DATABASE') 
    SQL_USER_NAME = os.getenv('SQL_USER_NAME') 
    SQL_PASSWORD = os.getenv('SQL_PASSWORD') 
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.getenv('BLOB_ACCOUNT') 
    BLOB_STORAGE_KEY = os.getenv('BLOB_STORAGE_KEY') 
    BLOB_CONTAINER = os.getenv('BLOB_CONTAINER') 
    
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    AUTHORITY = os.getenv('AUTHORITY')
    CLIENT_ID = os.getenv('CLIENT_ID')
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"