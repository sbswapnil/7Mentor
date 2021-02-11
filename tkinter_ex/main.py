import tkinter

top = tkinter.Tk()
# button = tkinter.Button(top, text ='Click me', )
# button.pack()
c = tkinter.Canvas(top, bg='yellow', height=500, width=500)
img = tkinter.PhotoImage(file='1.gif')
c.create_image(150, 150, image=img)
c.pack()
top.mainloop()