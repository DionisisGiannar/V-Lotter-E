#LOTTER-E by @Dionisis Giannaropoulos 
#Last update 24 Sept 2021

import random
import time
from tkinter import *
import tkinter 


class App():
    
    mainWindow = Tk()
    w, h = 0,0
    def __init__(self):
        self.mainWindow.geometry("1920x1080")
        self.mainWindow.title("Lottery")
     
        #self.mainWindow.geometry("%dx%d+0+0" % (self.w, self.h))
        
        #self.mainWindow = mainWindow

        self.mainWindow.attributes("-zoomed", True)
        self.w, self.h= int(self.mainWindow.winfo_screenwidth()), self.mainWindow.winfo_screenheight()
        print("width = "+str(self.w)+", height ="+ str(self.h))
        
        self.titleFrame = Frame(self.mainWindow,borderwidth=3,relief=RIDGE)
        self.create_TitleScreen()
        self.mainWindow.mainloop()


    def create_TitleScreen(self):
        self.titleFrame.pack()
        self.titleFrame.place(x=1,y=1,width=self.w,height=self.h)
        

        #Frame for the Label Title
        self.labelFrame = Frame(self.titleFrame,borderwidth=3, relief=RIDGE)
        self.labelFrame.pack(pady=400,anchor=CENTER)
        
        #self.labelFrame.place(x=760, y=375)
        self.titleLabel = Label(self.labelFrame, text="Welcome to The Lotter-E",)
        self.titleLabel.pack(pady=8,padx=5, side=TOP,expand=YES,fill=BOTH)
        self.titleLabel.place()
        self.titleLabel.config(font=('Ubuntu',25))

        #set the buttons
        self.playButton = Menubutton(self.titleFrame,text="Play Now", relief=GROOVE, width=12, height=1)
        self.playButton.config(font=('Ubuntu'))
        #playButton.grid()
        self.playButton.menu = Menu(self.playButton, tearoff=0)
        self.playButton["menu"] = self.playButton.menu
        self.playButton.menu.add_command(label="Text",command= self.textVersion, font=('Ubuntu'))
        self.playButton.menu.add_command(label="Text to speech", font=('Ubuntu'))
        
        self.playButton.pack()
        pBw=self.playButton.winfo_width()
        pBh=self.playButton.winfo_height()
        self.playButton.place(x=((self.w)/2)-pBw, y= ((self.h)/2)-pBh-50,anchor=CENTER)

    #Text Only Version
    def textVersion(self):
        for widget in self.mainWindow.winfo_children():
            widget.destroy()
            
        self.titleFrame.pack_forget()
        textOnlyVers = TextOnly()
        

#Class for the Text Only Version
class TextOnly(App):
    
    def __init__(App):
        App.titleTicket = Label(App.mainWindow, text='Ticket A',padx=200)
        App.titleTicket.config(font=('Ubuntu',25))
        App.titleTicket.pack(side=TOP)

        App.lotteryTicketFrame = Frame(App.mainWindow,borderwidth=3,relief=RIDGE)
        #App.lotteryTicketFrame.pack(side=TOP)#fill="both", expand=True
        #App.lotteryTicketFrame.place(x=1,y=1,width=1920,height=1080)
        App.lotteryTicketFrame.pack(side=TOP)
        #App.lotteryTicketFrame.place(x=640)   
        
        App.create_checkBox()

    def create_checkBox(App):
        checkButtonList = []
        checkBttnVarList = []
        for n in range(40):
            if n >=0 and n<=9:
                r=0
                c=int(n)
            elif n >=10 and n <=19:
                r=1
                c=int(n%10)
            elif n >=20 and n <=29:
                r=2
                c=int(n%20)
            elif n >=30 and n <=39:
                r=3
                c=int(n%30)

            checkBttnVarList.append(IntVar())
            checkButtonList.append(Checkbutton(App.lotteryTicketFrame, text=str(n+1), font=('Ubuntu'), variable=checkBttnVarList[n], onvalue=1, offvalue=0, height=3, width=2))
            
            checkButtonList[n].grid(row=r,column=c,padx=10, pady=15)

app = App()
