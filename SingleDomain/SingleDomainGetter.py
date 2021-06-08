from SingleDomain.GetNetDomains import get_net
from SQLConnector.Connect import connect
from SingleDomain.GetSingleDomain import get_single


def single_domain():
    conn = connect()
    _com = '.com'
    for link in get_net():
        link = str(link).replace('[\'', '')
        link = str(link).replace('\']', '')
        domain = link + '.com'
        get_single(domain, _com, link, conn)


if __name__ == "__main__":
    single_domain()
