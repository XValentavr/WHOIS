from SingleDomain.GetNetDomains import get_net
import whois

CHECKER = None


def get_single(name, dots, str, conn):
    try:
        av_domain = whois.whois(f"{name}")
        for key in av_domain.keys():
            if key == "status":
                if av_domain[key] != CHECKER:
                    list_domain = [(str, dots)]
                    query = "INSERT INTO org_zone (DomainName,ZoneOfDomain) VALUES(%s,%s)"
                    cursor = conn.cursor()
                    cursor.executemany(query, list_domain)
                    conn.commit()
    except whois.parser.PywhoisError:
        print(name)
