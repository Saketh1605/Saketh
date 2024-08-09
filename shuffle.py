import random
from tkinter import*
def shuffle_list():
    random.shuffle(lang)
    list1.delete(0,END)
    var1=Variable(value=lang)
    list1['listvariable']=var1


def show(e):
    l1['text']=list1.get(list1.curselection())


win=Tk()
win.title('My Shuffle Application')
win.geometry('600x400')

lang=['python','java','c++','sql','C','PHP']
var1=Variable(value=lang)

l1=Label(win,text='Select Item',font=30, fg='yellow')
l1.pack()

list1=Listbox(win,listvariable=var1)
list1.pack()
list1.bind('<<ListboxSelect>>',show)

b1=Button(win,text='Shuffle',command=shuffle_list)
b1.pack()

win.mainloop()
