import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from PIL import Image
from io import BytesIO
import pymysql
from pymysql import Error

path_for_photos="/home/saurabhlaptop/data/projects/abhyasika/admission_photos/"

# def _get_db():
#     try:
#         db = pymysql.connect(
#             host='localhost',
#             database='dnyansagar_abhyasika',
#             user='root',
#             password='root',
#             autocommit=True
#         )
#         return db
#     except pymysql.Error as e:
#         print("Error connecting to MySQL database:", e)
#         return None



def _get_db():
    try:
        db = pymysql.connect(
            host='192.168.29.50',
            database='dnyansagar_abhyasika_dev',
            user='user',
            password='root',
            autocommit=True
        )
        return db
    except pymysql.Error as e:
        print("Error connecting to MySQL database:", e)
        return None        
    

student_table_cols=['id','Name','Mobile','Address','Admission date','Photo','is_active']
student_payment_table_cols=['id','Date','Id','Method','Amount','Payment Month','Comment','MessageSent']
payment_details=['student_name','payment_date','payment_method','amount','payment_of_month','comment']

