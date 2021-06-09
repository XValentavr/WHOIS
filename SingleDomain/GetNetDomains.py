from SQLConnector.EC2Connector import connect


def get_net():
    conn = connect()
    query = "SELECT name_domain FROM isavailable"
    cursor = conn.cursor()
    cursor.execute(query)
    _net = cursor.fetchall()
    conn.commit()
    final_result = [list(i) for i in _net]
    return final_result
