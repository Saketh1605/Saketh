from tkinter import*
def change(e):
    r=redvar.get()
    g=greenvar.get()
    b=blurvar.get()
    l1['bg']=f'#{r:02x}{g:02x}{b:02x}'
win=Tk()
win.title('My colour selection')
win.geometry('600x600')

l1=Label(win,text='',bg='white', width=30)
l1.grid(row=0,column=0,columnspan=2)

redl=Label(win,text='red')
greenl=Label(win,text='green')
bluel=Label(win,text='blue')

redl.grid(row=1,column=0)
greenl.grid(row=2,column=0)
bluel.grid(row=3,column=0)

redvar=IntVar(value=0)
greenvar=IntVar(value=0)
blurvar=IntVar(value=0)

red_scale=Scale(win,orient=HORIZONTAL,variable=redvar,from_=0,to=255,command=change)
red_scale.grid(row=1,column=1)
green_scale=Scale(win,orient=HORIZONTAL,variable=greenvar,from_=0,to=255,command=change)
green_scale.grid(row=2,column=1)
blue_scale=Scale(win,orient=HORIZONTAL,variable=blurvar,from_=0,to=255,command=change)
blue_scale.grid(row=3,column=1)


win.mainloop()
