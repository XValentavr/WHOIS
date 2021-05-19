import string
from itertools import product
from DomainChecker import is_available
from SQLConnector.Connect import connect

LENGTH = 5


def create_alhpabet():
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    return alphabet_list


def create_domain(url):
    mylist = create_alhpabet()
    conn = connect()
    for chars in product(mylist, repeat=LENGTH):
        var = ''.join(chars)
        domain = var + url
        print(domain)
        is_available(domain, url, var, conn)

    return None
