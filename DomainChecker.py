import whois

CHECKER = None


def is_available(name, dots, str, conn):
    try:
        av_domain = whois.whois(f"{name}")
        for key in av_domain.keys():
            if key == "status":
                if av_domain[key] != CHECKER:
                    status = "in_use"
                    list_domain = [(str, status, dots)]
                    query = "INSERT INTO isavailable (name_domain,check_status,after_dot) VALUES(%s,%s,%s)"
                    cursor = conn.cursor()
                    cursor.executemany(query, list_domain)
                    conn.commit()
    except whois.parser.PywhoisError:
        print('')
