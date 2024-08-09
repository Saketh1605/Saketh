from tkinter import*
elapse_time=0
flag=True
def start():
    global elapse_time,flag
    flag=True
    update_time()
def update_time():
    global elapse_time,flag
    if flag==True:
        elapse_time +=1
        milli=elapse_time%1000
        sec=elapse_time//1000
        min=sec//60
        sec=sec%60

        l1['text']=f'{min:02d}:{sec:02d}:{milli:03d}'
        l1.after(1,update_time)


def Stop():
    global flag
    flag=False
def Reset():
    global elapse_time,flag
    elapse_time=0
    flag=False
    l1['text']='00:00:00'
win=Tk()
win.geometry('250x150')
win.title('My Stop watch')
l1=Label(win,text="00:00:00",font=('times new roman',45))
l1.grid(row=0,column=0,columnspan=3)

b1=Button(win,text='Start',command=start)
b1.grid(row=1,column=0)
b2=Button(win,text='Stop',command=Stop)
b2.grid(row=1,column=1)
b3=Button(win,text='Reset',command=Reset)
b3.grid(row=1,column=2)

win.mainloop()
