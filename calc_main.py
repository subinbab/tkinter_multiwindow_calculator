from tkinter_calculator1 import calculator1
from tkinter_calculator2 import calculator2
from tkinter import *
from PIL import Image,ImageTk
class mode1(calculator1):
    def __init__(self):
      super(calculator1,self).__init__()
      
class mode2(calculator2):
    def __init__(self):
         super(calculator2,self).__init__()
def modes1():
   y=mode1()
   y.con()
   y.entry()
   y.run()
def modes2():
   x=mode2()
   x.con()
   x.entry()
   x.run()

calculator=Tk()
photo = PhotoImage(file="calculator12.png")
calculator.iconphoto(False, photo)
calculator['bg']='#F0F0E6'
income=StringVar()
canvas=Canvas(calculator,width=200,height=300)

photo=Image.open('55664.png')
photo=ImageTk.PhotoImage(photo)
photo_label=Label(image=photo)
photo_label.image=photo
photo_label.grid(row=0,column=1)
text=Label(text='MECAL',font=('Times', 39, 'bold italic'),bg="#F0F0E6")
text.grid(column=1)

canvas.grid(columnspan=3,row=1)
calculator.title("MECAL")
def close1():
    calculator.destroy() 
    modes1() 
def close2():
    calculator.destroy() 
    modes2()
button=Button(calculator,text="BASIC",command=close1,width=10,bg="black",fg="white")
button.grid(column=0,row=2)
button=Button(calculator,text="SCIENTIFIC",command=close2,width=10,bg="black",fg="white")
button.grid(column=2,row=2,pady=15)

calculator.mainloop()

