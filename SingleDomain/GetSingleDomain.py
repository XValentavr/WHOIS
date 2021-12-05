"""
This module geta current availbale domain
"""
# standart imports
import whois

CHECKER = None


def get_single(name: str, dots: str, str: str, conn):
    """
    gets available domain
    :param name: str
    :param dots: str
    :param str: str
    :param conn: database connection
    """
    try:
        av_domain = whois.whois(f"{name}")
        for key in av_domain.keys():
            if key == "status":
                if av_domain[key] != CHECKER:
                    list_domain = [(str, dots)]
                    query = "INSERT INTO biz_zone (DomainName,ZoneOfDomain) VALUES(%s,%s)"
                    cursor = conn.cursor()
                    cursor.executemany(query, list_domain)
                    conn.commit()
    except whois.parser.PywhoisError:
        print('An error occured')
