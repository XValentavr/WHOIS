"""
This module get .net available domains
"""

# project imports
from SQLConnector.Connect import connect


def get_net():
    """
    gets .net available domains
    """
    conn = connect()
    query = "SELECT DISTINCT DomainName FROM info_zone"
    cursor = conn.cursor()
    cursor.execute(query)
    _net = cursor.fetchall()
    conn.commit()
    final_result = [list(i) for i in _net]
    return final_result
