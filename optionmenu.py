from tkinter import *
def change(e):
    listvar=Variable(value=dict1[var1.get()])
    l1.delete(0,END)
    l1['listvariable']=listvar
win=Tk()
win.title('My Option Menu')
win.geometry('600x400')
dict1={'langs':['python','java','c','c++'],
       'databases':['oracle','sql server','mysql'],
       'clouds':['AWS','SalesForce','MS Asure']}
var1=StringVar(value='langs')
opt1=OptionMenu(win, var1,*dict1.keys(),command=change)
opt1['fg']='blue'
opt1.pack()

listvar=Variable(value=dict1['langs'])
l1=Listbox(win,listvariable=listvar)
l1.pack()



win.mainloop()
