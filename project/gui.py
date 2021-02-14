from tkinter import *
from tkinter import ttk
from project.main import Sql


class GUI:

    def __init__(self, root1):
        self.root = root1
        self.obj_sql = Sql()
        self.root.title('Student Managment System')

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        # setting tkinter window size
        self.root.state("zoomed")
        self.root.geometry("%dx%d+0+0" % (width, height))

        title = Label(self.root, text='Student Managment System', pady=5, fg='white', bg='blue',
                      font=('times new roman', 40, 'bold'))
        title.pack(side=TOP, fill=X)

        # Frame 1
        frame_1 = Frame(self.root, bd=4, relief=RIDGE, bg='crimson')
        frame_1.place(x=80, y=100, height=650, width=550)
        title_f1 = Label(frame_1, text='Student Information', bg='blue', fg='white',
                         font=('times new roman', 30, 'bold'))
        title_f1.grid(row=0, columnspan=2, padx=10, pady=10, ipadx=15, ipady=5)

        # Frame 2
        frame_2 = Frame(self.root, bd=4, relief=RIDGE, bg='crimson')
        frame_2.place(x=700, y=100, height=650, width=750)
        # title_f2 = Label(frame_2, text='Student Details', bg='blue', fg='white', font=('times new roman', 30, 'bold'))
        # title_f2.grid(row=0, columnspan=2, padx=10, pady=10, ipadx=15, ipady=5)

        name = Label(frame_1, text='Name : ', bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        year = Label(frame_1, text='Year : ', bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        stream = Label(frame_1, text='Stream : ', bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        phone_no = Label(frame_1, text='Phone Number : ', fg='white', bg='crimson',
                         font=('times new roman', 20, 'bold'))
        subject_1 = Label(frame_1, text='Subject_1 Mark : ', fg='white', bg='crimson',
                          font=('times new roman', 20, 'bold'))
        subject_2 = Label(frame_1, text='Subject_2 Mark : ', fg='white', bg='crimson',
                          font=('times new roman', 20, 'bold'))
        subject_3 = Label(frame_1, text='Subject_3 Mark : ', fg='white', bg='crimson',
                          font=('times new roman', 20, 'bold'))
        marks = Label(frame_1, text='Marks : ', fg='white', bg='crimson', font=('times new roman', 20, 'bold'))
        percentage = Label(frame_1, text='Percentage : ', fg='white', bg='crimson',
                           font=('times new roman', 20, 'bold'))

        #  Variables

        self.var_name = StringVar()
        self.var_year = StringVar()
        self.var_stream = StringVar()
        self.var_phone_no = StringVar()
        self.var_sub1_marks = StringVar()
        self.var_sub2_marks = StringVar()
        self.var_sub3_marks = StringVar()
        self.var_marks = StringVar()
        self.var_percentage = StringVar()

        name.grid(column=0, row=1, sticky=W, padx=10, pady=5)
        year.grid(column=0, row=2, sticky=W, padx=10, pady=5)
        stream.grid(column=0, row=3, sticky=W, padx=10, pady=5)
        phone_no.grid(column=0, row=4, sticky=W, padx=10, pady=5)
        subject_1.grid(column=0, row=5, sticky=W, padx=10, pady=5)
        subject_2.grid(column=0, row=6, sticky=W, padx=10, pady=5)
        subject_3.grid(column=0, row=7, sticky=W, padx=10, pady=5)
        marks.grid(column=0, row=8, sticky=W, padx=10, pady=5)
        percentage.grid(column=0, row=9, sticky=W, padx=10, pady=5)

        name = Entry(frame_1, textvariable=self.var_name, font=('times new roman', 20, 'bold'), bd=5, relief=GROOVE)
        year = Entry(frame_1, textvariable=self.var_year, font=('times new roman', 20, 'bold'), bd=5, relief=GROOVE)
        stream = Entry(frame_1, textvariable=self.var_stream, font=('times new roman', 20, 'bold'), bd=5, relief=GROOVE)
        phone_no = Entry(frame_1, textvariable=self.var_phone_no, font=('times new roman', 20, 'bold'), bd=5,
                         relief=GROOVE)
        sub_1 = Entry(frame_1, textvariable=self.var_sub1_marks, font=('times new roman', 20, 'bold'), bd=5,
                      relief=GROOVE)
        sub_2 = Entry(frame_1, textvariable=self.var_sub2_marks, font=('times new roman', 20, 'bold'), bd=5,
                      relief=GROOVE)
        sub_3 = Entry(frame_1, textvariable=self.var_sub3_marks, font=('times new roman', 20, 'bold'), bd=5,
                      relief=GROOVE)
        marks = Entry(frame_1, textvariable=self.var_marks, font=('times new roman', 20, 'bold'), bd=5, relief=GROOVE)
        percentage = Entry(frame_1, textvariable=self.var_percentage, font=('times new roman', 20, 'bold'), bd=5,
                           relief=GROOVE)

        name.grid(column=1, row=1, padx=5, pady=5)
        year.grid(column=1, row=2, padx=5, pady=5)
        stream.grid(column=1, row=3, padx=5, pady=5)
        phone_no.grid(column=1, row=4, padx=5, pady=5)
        sub_1.grid(column=1, row=5, padx=5, pady=5)
        sub_2.grid(column=1, row=6, padx=5, pady=5)
        sub_3.grid(column=1, row=7, padx=5, pady=5)
        marks.grid(column=1, row=8, padx=5, pady=5)
        percentage.grid(column=1, row=9, padx=5, pady=5)

        # Frame btn

        frame_btn = Frame(frame_1, bd=4, relief=RIDGE, bg='CRIMSON')
        frame_btn.place(x=10, y=580, width=520)

        addbtn = Button(frame_btn, command=self.add_student, text='ADD', width=10).grid(row=0, column=0, padx=25,
                                                                                        pady=10)
        updatebtn = Button(frame_btn, command=self.update_student, text='UPDATE', width=10).grid(row=0, column=1,
                                                                                                 padx=20,
                                                                                                 pady=10)
        deletebtn = Button(frame_btn, command=self.delete_student, text='DELETE', width=10).grid(row=0, column=2,
                                                                                                 padx=20, pady=10)
        clearbtn = Button(frame_btn, command=self.clear, text='CLEAR', width=10).grid(row=0, column=3, padx=20, pady=10)

        # Table Frame

        frame_table = Frame(frame_2, bd=4, relief=RIDGE, bg='crimson')
        frame_table.place(x=10, y=80, height=550, width=720)

        scroll_x = Scrollbar(frame_table, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame_table, orient=VERTICAL)
        self.student_table = ttk.Treeview(frame_table, columns=(
            'Id', 'Name', 'Year', 'Stream', 'Phone No', 'Sub1 Marks', 'Sub2 Marks', 'Sub3 Marks', 'Marks',
            'Percentage'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Id', text='Id')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Year', text='Year')
        self.student_table.heading('Stream', text='Stream')
        self.student_table.heading('Phone No', text='Phone No')
        self.student_table.heading('Sub1 Marks', text='Sub1 Marks')
        self.student_table.heading('Sub2 Marks', text='Sub2 Marks')
        self.student_table.heading('Sub3 Marks', text='Sub3 Marks')
        self.student_table.heading('Marks', text='Marks')
        self.student_table.heading('Percentage', text='Percentage')
        self.student_table['show'] = 'headings'
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease-1>', self.get_row)

        self.getData()

     
    def add_student(self):
        query = 'insert into student(Name, Year, Stream, Phone_No, Sub_1_Mark, Sub_2_Mark, Sub_3_Mark, ' \
                'Marks, Percentage) values("%s", "%s", "%s", "%s", "%s", "%s", "%s","%s", "%s")' % (
                    self.var_name.get(), self.var_year.get(), self.var_stream.get(), self.var_phone_no.get(),
                    self.var_sub1_marks.get(), self.var_sub2_marks.get(), self.var_sub3_marks.get(),
                    self.var_marks.get(),
                    self.var_percentage.get())

        self.obj_sql.insert(query)
        self.getData()
        self.clear()

    def update_student(self):

        c_row = self.student_table.focus()
        values = self.student_table.item(c_row)
        row = values['values']
        query = 'update student set Name="%s", Year="%s", Stream="%s", Sub_1_mark="%s", ' \
                'Sub_2_mark="%s", Sub_3_mark="%s",Marks="%s", Percentage="%s", Phone_No="%s" where Id = %d' % (
                    self.var_name.get(), self.var_year.get(), self.var_stream.get(),
                    self.var_sub1_marks.get(), self.var_sub2_marks.get(), self.var_sub3_marks.get(),
                    self.var_marks.get(),
                    self.var_percentage.get(), self.var_phone_no.get(), row[0])

        self.obj_sql.update(query)
        self.getData()
        self.clear()

    def delete_student(self):
        c_row = self.student_table.focus()
        values = self.student_table.item(c_row)
        row = values['values']
        query = 'delete from student where Id=%d' % (row[0])
        self.obj_sql.delete(query)

        self.getData()
        self.clear()

    def getData(self):
        query = 'select * from student'
        results = self.obj_sql.show(query)

        if len(results) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in results:
                self.student_table.insert('', END, values=row)

    def clear(self):
        self.var_name.set(''), self.var_year.set(''), self.var_stream.set(''), self.var_phone_no.set(''),
        self.var_sub1_marks.set(''), self.var_sub2_marks.set(''), self.var_sub3_marks.set(''), self.var_marks.set(''),
        self.var_percentage.set('')

    def get_row(self, event):
        c_row = self.student_table.focus()
        values = self.student_table.item(c_row)
        row = values['values']
        self.var_name.set(row[1]), self.var_year.set(row[2]), self.var_stream.set(row[3]), self.var_phone_no.set(
            row[4]),
        self.var_sub1_marks.set(row[5]), self.var_sub2_marks.set(row[6]), self.var_sub3_marks.set(
            row[7]), self.var_marks.set(row[8]),
        self.var_percentage.set(row[9])


if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.mainloop()
