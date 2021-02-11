# rollno, name, marks

while True:
    roll_no = None
    name = None
    marks = None
    ch = 'N'

    print('Enter the Roll number, Name and Marks of the student: ')
    roll_no = input('Roll Number: ')
    name = input('Name: ')
    marks = input('Marks: ')

    print(f'{roll_no} {name} {marks}')
    print('Do you want to enter another student data.... (Y/N)')
    ch = input('enter Y or N')
    if ch=='N'or ch=='n':

        with open('studinfo.txt', 'a') as w:
            w.write(f'\n{roll_no.ljust(10, " ")} {name.ljust(10, " ")} {marks}')
            
        break

