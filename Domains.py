import string
from itertools import product
from DomainChecker import is_available

LENGTH = 5


def create_alhpabet():
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    return alphabet_list


def create_domain(url):
    mylist = create_alhpabet()
    for chars in product(mylist, repeat=LENGTH):
        var = ''.join(chars)
        domain = var + url
        is_available(domain, url, var)

    return None
