from project.connect import connection


class Sql:
    sql_create_table = 'create table if not exists student(Id int AUTO_INCREMENT, Name char(20) not null, Year char(' \
                       '20) not null, ' \
                       'Stream char(20) not null, Phone_No char(20) not null, Sub_1_mark char(20) not null, ' \
                       'Sub_2_mark char(20) not null, Sub_3_mark char(20) not null,Marks char(20) not null, ' \
                       'Percentage char(20) not null,     PRIMARY KEY (Id)) '

    def __init__(self):
        self.conn = connection()
        self.curr = self.conn.cursor()
        self.createTable(Sql.sql_create_table)

    def excut(self, sqlQuery):
        try:
            self.curr.execute(sqlQuery)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return e, False

    def createTable(self, sqlQuery):
        if self.excut(sqlQuery):
            print('Table created successfully...')
        else:
            print('error while creating table')

    def insert(self, sqlQuery):
        if self.excut(sqlQuery):
            print('Values inserted successfully...')
        else:
            print('error while inserting values...')

    def update(self, sqlQuery):
        if self.excut(sqlQuery):
            print('Values updated successfully...')
        else:
            print('error while updating values...')

    def delete(self, sqlQuery):
        if self.excut(sqlQuery):
            print('Value  deleted successfully...')
        else:
            print('error while deleting table')

    def show(self, sqlQuery):
        try:
            self.curr.execute(sqlQuery)
            result = self.curr.fetchall()
            return result
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    obj = Sql()
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

            obj.createTable(sqlQuery=sql)

        if ch == 2:

            while True:
                name = input('enter Name: ')
                age = int(input('enter Age: '))
                marks = float(input('enter Marks: '))

                sql = 'insert into student values(\'%s\', %d, %f)' % (name, age, marks)
                obj.excut(sqlQuery=sql)

                ch1 = input('Do you want to enter another info(Y/N) : ')

                if ch1 == 'No' or ch1 == 'no':
                    break

        if ch == 3:
            sql = 'update student set f_name="ABCD" where marks = 87'
            obj.update(sqlQuery=sql)

        if ch == 4:
            sql = 'delete from student where f_name="ABCD"'
            obj.delete(sqlQuery=sql)

        if ch == 5:
            sql = 'select * from student'
            r = obj.show(sqlQuery=sql)
            for name, age, marks in r:
                print(name, age, marks)

        if ch not in range(1, 6):
            break
