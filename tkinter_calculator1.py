from tkinter import *
#this class is for the basic calculator
class calculator1(Tk):
    #class constructor
    def __init__(self):
        Tk.__init__(self)
        b=[1,2,3,4,5,6,7,8,9,0] 
    def con(self):
        photo = PhotoImage(file="calculator12.png")
        self.iconphoto(False, photo)
        self.string=StringVar()#entry string variable
        self.string1=StringVar()
        self.title("MECALL")
        self.geometry("252x272")
        self.config(bg="white")

        entry=Entry(self,
		width=32,
		border=0,
		font=('helvetica', 10),
		justify=RIGHT,
		textvariable=self.string)
        entry.grid(row=0,columnspan=35)

        entry1=Entry(self,
		width=15,
		border=0,
		font=('helvetica', 20),
		justify=RIGHT,
		textvariable=self.string1)
        entry1.grid(row=1,columnspan=35)

    def entry(self):
        x=IntVar()
        self.name=[7,8,9,"AC",4,5,6,"/",1,2,3,"-",0,".","=","+","CLEAR","BACK","GAME","*"]#buttons list
        i=0
        padx=17
        pady=10
        row=2
        column=0
        for txt in self.name:
            
            print(i)
            if(i==4): #loop for arranging each button in rows
                row=3
                
                column=0
            if(i==8):
                row=4
                
                column=0
            if(i==12):
                row=5
                column=0
            if(i==16):
                row=6
                column=0
            if(i==20):
                row=7
                column=0
            else:
                button=Button(self,padx=padx,pady=pady,width=3,text=txt,command=lambda txt=txt:self.calculate(txt))
                button.grid(row=row,column=column)
                
            
            column=column+1
            i=i+1        
    def calculate(self,text):  #function of each button
        if(str(text)=="="):
            try:
               self.string1.set(eval(self.string.get()))
            except:
                self.string1.set("INVALID INPUT")
        elif(str(text)=="AC"):
            self.string.set("")
        elif(str(text)=="CLEAR"):
            self.string.set(self.string.get()[0:-1])
        else:
            self.string.set(self.string.get()+(str(text)))      
            
    def run(self):
        self.mainloop()

