import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqlserver20210405.database.windows.net' #update
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'sqldb20210405' #update
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'dbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'blob20210405' #update
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'f1hN4QPC17A8izYOsMe1baQ7EiXmk8cXMCmozLapjOckyAHUBv77lT/U9k+SD2vEfXbjKDNza5lKBoYrxuiBjw==' #update
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    CLIENT_SECRET = "EM913Ip.XvNyr4Qv~L~.o3aU.65.T.7uKJ" # update: certificates & secrets from App Registration
    AUTHORITY = "https://login.microsoftonline.com/hwdgrmygmail.onmicrosoft.com"
    CLIENT_ID = "0e474e20-b2bc-4f33-95d6-7fe8dd478706" # update: application (client) ID from App Registration
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"

