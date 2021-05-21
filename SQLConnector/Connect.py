import mysql
from mysql.connector import MySQLConnection, Error
import pymysql


def connect():
    try:
        conn = pymysql.connect(host='domain-database.cluster-c4e6le3yokkr.us-east-2.rds.amazonaws.com', user='admin',
                               password='xvalentavr')

    except Error as e:
        print('Error:', e)

    finally:
        return conn
