from tkinter import*
import time

def myclock():
    watch= time.strftime('%I:%M:%S')
    l1['text']=watch
    l1.after(100,myclock)
win=Tk()
win.geometry('600x400')
win.title('My Digital Clock')

l1=Label(win,bg='red',font=('Times new roman',50))
l1.pack(fill=BOTH,expand=True)

myclock()
win.mainloop()
