import os
from dotenv import load_dotenv

load_dotenv()
timeout = 10

# def fetch_stock_data_wrapper():
#     Stock.fetch_stock_data() 
# JOBS                    =       [
#                                     {
#                                         'id': 'fetch_stock_data',
#                                         'func': fetch_stock_data_wrapper,
#                                         'trigger': 'cron',
#                                         'hour': 0,
#                                         'minute': 0
#                                     }
#                                 ]

class Config:
    # SECRET_KEY            =       os.getenv('SECRET_KEY')

    DB_CHARSET              =       os.getenv('DB_CHARSET')
    DB_NAME                 =       os.getenv('DB_NAME')
    DB_HOST                 =       os.getenv('DB_HOST')
    DB_PASSWORD             =       os.getenv('DB_PASSWORD')
    DB_PORT                 =       int(os.getenv('DB_PORT'))
    DB_USER                 =       os.getenv('DB_USER')
    DB_CONNECT_TIMEOUT      =       timeout
    DB_READ_TIMEOUT         =       timeout
    DB_WRITE_TIMEOUT        =       timeout

    BRAND_NAME              =       "π-AMS"
