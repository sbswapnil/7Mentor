import MySQLdb


def connection():
    try:
        conn = MySQLdb.connect('localhost', 'root', '', 'student_managment_system')
        return conn
    except Exception as e:
        print(e)
