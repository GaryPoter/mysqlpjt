

def get_insert_statement(table=None, **kwargs):
    sql = "insert into "
    sql += (table + "(")
    for key in kwargs.keys():
        sql += (key + ",")
    sql = sql[:-1]
    sql += ") VALUES ("
    for key in kwargs.keys():
        sql += ("'" + kwargs[key] + "',")
    sql = sql[:-1]
    sql += ')'
    print(sql)
    return sql