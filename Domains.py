"""
This module creates all possible domains with length 5 using alphabet
"""
# project imports
import string
from itertools import product
# local imports
from MainDomain.DomainChecker import is_available
from SQLConnector.Connect import connect

LENGTH = 5


def create_alhpabet():
    """
    create alphabet

    """
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string.lower())
    return alphabet_list


def create_domain(url: str):
    """
    creates domains with length 5 using alphabet
    :param url:str
    """
    mylist = create_alhpabet()
    conn = connect()
    for chars in product(mylist, repeat=LENGTH):
        var = ''.join(chars)
        domain = var + url
        is_available(domain, url, var, conn)
