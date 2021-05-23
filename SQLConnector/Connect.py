import mysql
from mysql.connector import MySQLConnection, Error
import PyMySQL


def connect():
    try:

        conn = pymysql.connect(host='domain-database.cluster-c4e6le3yokkr.us-east-2.rds.amazonaws.com', port=3306,
                               user='admin',
                               password='xvalentavr', database='domain_checker_db', charset='utf8mb4')
    except Error as e:
        print('Error:', e)

    finally:
        return conn
