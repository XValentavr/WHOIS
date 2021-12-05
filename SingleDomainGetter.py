"""
This module gets domain in zone that are set previously
"""

# local imports
from SingleDomain.GetNetDomains import get_net
from SQLConnector.Connect import connect
from SingleDomain.GetSingleDomain import get_single

FINAL_ZONE = '.biz'


def single_domain():
    """
    set domain zone and gets if domain is available
    :return:
    """
    conn = connect()
    _biz = '.biz'
    i = 0
    while i <= 20:
        for link in get_net():
            link = str(link).replace('[\'', '')
            link = str(link).replace('\']', '')
            domain = link + FINAL_ZONE
            get_single(domain, _biz, link, conn)
    i += 1


if __name__ == "__main__":
    single_domain()
