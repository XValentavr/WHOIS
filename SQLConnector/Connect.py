"""
This module create database connection
"""

# standart imports
import mysql

# local imports
from mysql.connector import MySQLConnection, Error


def connect():
    """
    create local database connection
    :return:
    """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='domains',
                                       user='root',
                                       password='root')

    except Error as e:
        print('Error:', e)

    finally:
        return conn
