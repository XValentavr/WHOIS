from SingleDomain.GetNetDomains import get_net
from SQLConnector.EC2Connector import connect
from SingleDomain.GetSingleDomain import get_single

FINAL_ZONE = '.org'


def single_domain():
    conn = connect()
    _org = '.org'
    for link in get_net():
        link = str(link).replace('[\'', '')
        link = str(link).replace('\']', '')
        domain = link + FINAL_ZONE
        get_single(domain, _org, link, conn)


if __name__ == "__main__":
    single_domain()
