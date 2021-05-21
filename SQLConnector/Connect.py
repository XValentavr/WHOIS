import mysql
from mysql.connector import MySQLConnection, Error
import mysql.connector
import boto3
import os


def connect():
    ENDPOINT = " domain-database.cluster-c4e6le3yokkr.us-east-2.rds.amazonaws.com "
    PORT = "3306"
    USR = "admin"
    REGION = "us-east-2a"
    DBNAME = "domain_checker_db"
    os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'
    session = boto3.Session(profile_name='default')
    client = session.client('rds')
    try:
        conn = mysql.connector.connect(host=ENDPOINT, user=USR, passwd='xvalentavr', port=PORT, database=DBNAME)
    except Error as e:
        print('Error:', e)

    finally:
        return conn
