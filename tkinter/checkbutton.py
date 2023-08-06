from tkinter import *
root = Tk()


v= IntVar()

label = Label(text='AAaysh', textvariable=v)
label.pack()

entry = Entry(textvariable=v)
entry.pack()



# Check button
a = IntVar()
def yes_or_not():
    print(a.get())
c = Checkbutton(text='Are you ready', command=yes_or_not, variable=a)
c.pack()


root.mainloop()


