from psycopg2.extras import RealDictCursor
from app.db.db_init import config, connect_db

connection = connect_db()

def list_all_product(limit, page):
    """
       - Expose all data of product with Pagination
        Args:
           limit (Union[str, None] = None): Query Param for specific limit of data in particular page
           page (Union[str, None] = None): Query Param for particular no. of page
        Returns:
           list of all product with proper pagination in json format
    """
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    table_name = config.table_name
    query = ""
    if page:
        offset = (int(page) - 1) * 10 + 1
        query = "select * from " + table_name + " limit " + limit + " offset " + str(offset) + ";"
    else:
        query = "select * from " + table_name + ";"
    print(query)
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)
    return res
