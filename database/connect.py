import MySQLdb


def connection():
    try:
        conn = MySQLdb.connect('localhost', 'root', '', 'collage')
        return conn
    except Exception as e:
        print(e)
