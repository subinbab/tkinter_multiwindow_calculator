from tkinter import *
from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor,sinh,cosh,tanh,sqrt
class calculator2(Tk):
    def __init__(self):
        Tk.__init__(self)
        b=[1,2,3,4,5,6,7,8,9,0] 
    def con(self):

        photo = PhotoImage(file="calculator12.png")
        self.iconphoto(False, photo)

        self.string1=StringVar()#entry string variable
        self.string2=StringVar()
        self.title("MECALL")
        self.geometry("295x334")
        self.config(bg="white")
        entry1=Entry(self,
		width=19,
		border=0,
		font=('helvetica', 20),
		justify=RIGHT,
		textvariable=self.string1)
        entry1.grid(row=0,columnspan=35)
        
        entry2=Entry(self,
		width=10,
		border=0,
		font=('helvetica', 39),
		justify=RIGHT,
		textvariable=self.string2)
        entry2.grid(row=1,columnspan=35)
    def entry(self):
        x=IntVar()
        self.name=["cosec","sec","cot","sqrt","radians","sin","cos","tan","sinh","cosh","tanh"
        ,"**","(",")","log",7,8,9,"CLEAR","AC",4,5,6,"*","/",1,2,3,"+","-",0,".","e","pi","="]#buttons list
        i=0
        padx=15
        pady=5
        row=2
        column=0
        print("lenghth :",len(self.name))
        for txt in self.name:
            if(i==5): #loop for arranging each button in rows
                row=3
                
                column=0
            if(i==10):
                row=4
                
                column=0
            if(i==15):
                row=5
                column=0
            if(i==20):
                row=6
                column=0
            if(i==25):
                row=7
                column=0
            if(i==30):
                row=8
                column=0
            if(i==35):
                row=9
                column=0
            else:
                button=Button(self,padx=padx,pady=pady,width=3,text=txt,command=lambda txt=txt:self.calculate(txt))
                button.grid(row=row,column=column)
                
            
            column=column+1
            i=i+1        
    def calculate(self,text):  #function of each button
        if(str(text)=="="):
            try:
               self.string2.set(eval(self.string1.get()))
            except:
                self.string1.set("INVALID INPUT")
        elif(str(text)=="AC"):
            self.string1.set("")
            self.string2.set("")
        elif(str(text)=="CLEAR"):
            self.string1.set(self.string1.get()[0:-1])
        elif(str(text)=="mode"):
            self.string1.set("1.gradient 2.radians")
        else:
            self.string1.set(self.string1.get()+(str(text)))      
            
    def run(self):
        self.mainloop()