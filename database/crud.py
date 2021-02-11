from database.connect import connection

conn = connection()
curr = conn.cursor()


def excut(sqlQuery):
    try:
        curr.execute(sqlQuery)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False


def createTable(sqlQuery):
    if excut(sqlQuery):
        print('Table created successfully...')
    else:
        print('error in creating table')


def insert(sqlQuery):
    if excut(sqlQuery):
        print('Values inserted successfully...')
    else:
        print('error while inserting values...')


def update(sqlQuery):
    if excut(sqlQuery):
        print('Values updated successfully...')
    else:
        print('error while updating values...')


def delete(sqlQuery):
    if excut(sqlQuery):
        print('Value  deleted successfully...')
    else:
        print('error while deleting table')


def show(sqlQuery):
    try:
        curr.execute(sqlQuery)
        result = curr.fetchall()
        return result
    except Exception as e:
        print(e)
        return False


while True:
    print('1) Create Table\n'
          '2) Insert\n'
          '3) Update\n'
          '4) Delete\n'
          '5) Show\n'
          '6) Exit\n'
          '-------------------------------------')
    ch = int(input('Enter Your Choice : '))

    if ch == 1:
        # sql = input('Enter query to create table : ')
        sql = 'create table student1(name char(20) not null, age int not null,marks float)'
        print(sql)

        createTable(sqlQuery=sql)

    if ch == 2:

        while True:
            name = input('enter Name: ')
            age = int(input('enter Age: '))
            marks = float(input('enter Marks: '))

            sql = 'insert into student values(\'%s\', %d, %f)' % (name, age, marks)
            excut(sqlQuery=sql)

            ch1 = input('Do you want to enter another info(Y/N) : ')

            if ch1 == 'No' or ch1 == 'no':
                break

    if ch == 3:
        sql = 'update student set f_name="ABCD" where marks = 87'
        update(sqlQuery=sql)

    if ch == 4:
        sql = 'delete from student where f_name="ABCD"'
        delete(sqlQuery=sql)

    if ch == 5:
        sql = 'select * from student'
        r = show(sqlQuery=sql)
        for name, age, marks in r:
            print(name, age, marks)

    if ch not in range(1, 6):
        break
