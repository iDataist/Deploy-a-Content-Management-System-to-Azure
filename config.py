import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'db-server-20210402.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'db-20210402'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'dbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'blob20210402'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'P/B0o4hPL90wLyI+6w9C7FMGaibN09NszHpW6RG9nZlYF5YnF5jbx+zd8TTr1aQPQl6iIhMC7wGyjFFCNlA7rQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    CLIENT_SECRET = "gQs.mxTeHVw.rLLBK9bt54M8Er-8c6~1jV"
    AUTHORITY = "https://login.microsoftonline.com/hwdgrmygmail.onmicrosoft.com"
    CLIENT_ID = "cefd54a1-1a2e-4600-a04f-072a4df822f2"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"

