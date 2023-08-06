from tkinter import *
root = Tk()
root.geometry('600x500')
# root.configure(bg='black')


# Main menu
m=Menu()


# Add the child menu under the the main menu
mm=Menu(m)
# Add the menu options
mm.add_command(label='aaysh',activebackground='black', activeforeground='green')
root.config(menu=m)

# Add the name  of the menu
m.add_cascade(menu=mm, label='add')








v=Label(text='basnte',anchor=CENTER,bg='black', fg='white',pady=22,padx=22)
v.pack(anchor=CENTER)





root.mainloop()