# Statement for enabling the development environment
# Enabling the development environment
DEBUG = True
DB_USER = 'zuknshrpyxbdjg'
DB_PASS = 'b1651a9c9cd0adcb24f9dc4414f5f635f37ddaddebb8ca46dc86bd3d0008ecbc'
DB_HOST = 'ec2-23-21-162-90.compute-1.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'd9jegcm8m9atr5'

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'mysql://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+'/'+DB_NAME
SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{pw}@{url}:{port}/{db}'.format(user=DB_USER,pw=DB_PASS,url=DB_HOST,db=DB_NAME, port=DB_PORT)
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "thesecretsss"

LOGGING_FORMAT = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
# LOGGING_LOCATION = 'logs/error.log'
