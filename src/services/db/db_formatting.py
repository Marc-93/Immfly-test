def format_query(select, from_db_name, where="", order_by="", limit=0):
    """Formats a SQL query with Select, from, where and order by params.

    :param select: Filtered result
    :param from_db_name: Database.table
    :param where: Query filter
    :param order_by: result order
    :return: Formatted query
    """
    if where == "" and order_by == "":
        return f"SELECT {select} FROM {from_db_name}"
    elif where != "" and order_by == "":
        return f"SELECT {select} FROM {from_db_name} WHERE {where}"
    elif where == "" and order_by != "":
        return f"SELECT {select} FROM {from_db_name} ORDER BY {order_by}"
    elif where != "" and order_by != "":
        return f"SELECT {select} FROM {from_db_name} WHERE {where} ORDER BY {order_by}"
    elif where != "" and order_by != "" and limit != 0:
        return f"SELECT {select} FROM {from_db_name} WHERE {where} ORDER BY {order_by} LIMIT {limit}"
