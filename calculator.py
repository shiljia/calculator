
from tkinter import*
from functools import partial

root=Tk()
root.title('calculator')

tb=Entry(root,font=('arial',23))
tb.grid(row=0,column=0,columnspan=4)

def click():
    if(t=='C'):
        tb.delete(0,END)
    elif(t=='X'):
        text=tb.get()[:-1]
        tb.delete(0,END)
        tb.insert(0,text)
    elif(t=='='):
        ans=eval(tb.get())
        tb.delete(0,END)
        tb.insert(0,ans)
    else:
        tb.insert(END,t)

btn=['C','(',')','/',
     '7','8','9','*',
     '4','5','6','-',
     '1','2','3','+',
     'X','0','.','=']

r=1
c=0
clr='gray'

for i in btn:
    if(i=='C' or i=='X'):
        clr='red'
    elif(i=='='):
        clr='green'
    else:
        clr='gray'
        
    clk=partial(click,i)
    
    b=Button(root,text=i,bg=clr,width=5,height=2,font=('arial',19),command=clk)
    b.grid(row=r,column=c)

    if(c==3):
        r+=1
        c=0
    else:
        c+=1
    

root.mainloop()
