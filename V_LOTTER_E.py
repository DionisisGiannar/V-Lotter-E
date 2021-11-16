#LOTTER-E by @Dionisis Giannaropoulos 
#Last update 14 Oct 2021

import random
import time
import threading
from tkinter import * 
from tkinter import messagebox
import tkinter 
import mysql.connector
from mysql.connector import errorcode
import atexit  
import screeninfo

class App():
    submition = []
    sub_special = None

    #mysql connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="DionGiannar",
        password="Password1!",
        database= "VLE_Submitions"
    )
    
    
    
    mainWindow = Tk()
    w, h = 0,0

   

        
    def __init__(self):
        self.create_database(self.mydb.cursor())
        
        self.mainWindow.geometry("1920x1080")
        self.mainWindow.title("Lottery")
     
        #self.mainWindow.geometry("%dx%d+0+0" % (self.w, self.h))
        
        #self.mainWindow = mainWindow

        self.mainWindow.attributes("-zoomed", True)
        print(screeninfo.get_monitors())
        monitors = 0
        monitors_x = 0
        monitors_y = 0
        for m in screeninfo.get_monitors():
            monitors += 1 
            monitors_x += m.x
            monitors_y += m.y
        
        self.w = int(self.mainWindow.winfo_screenwidth()- monitors_x)
        self.h = int(self.mainWindow.winfo_screenheight()- monitors_y)
            
        
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
        self.textOnlyVers = TextOnly()
    
    def create_database(self, cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format('VLE_Submitions'))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            

        try:
            cursor.execute("USE {}".format('VLE_Submitions'))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format('VLE_Submitions'))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(cursor)
                print("Database {} created successfully.".format('VLE_Submitions'))
                self.mydb.database = 'VLE_Submitions'
            else:
                print(err)
            exit(1)

    # deletes tables submition
    def del_submition(App):
        print("DELETING TABLE!")
        mycursor = App.mydb.cursor()
        mycursor.execute("DROP TABLE submitions")


#Class for the Text Only Version
class TextOnly(App):
    checkButtonList = []
    checkBttnVarList = []
    
    
    def __init__(App):
        App.titleTicket = Label(App.mainWindow, text='Ticket A',padx=200)
        App.titleTicket.config(font=('Ubuntu',25))
        App.titleTicket.pack(side=TOP)

        App.ticketFrameA = LabelFrame(App.mainWindow, text='Select 6 numbers', font=('Ubuntu'),borderwidth=3,relief=RIDGE)
        App.ticketFrameA.pack(side=TOP)

        App.ticketFrameB = LabelFrame(App.mainWindow, text='Select 1 special number', font=('Ubuntu'),borderwidth=3,relief=RIDGE)
        App.ticketFrameB.pack(side=TOP)

        App.message_Frame = LabelFrame(App.mainWindow, text='Warning', font=('Ubuntu'))
        App.message = Label(App.message_Frame, font=('Ubuntu'))

        App.create_checkBox()
        App.create_Buttons()

    #Function to create the check boxes (and the initiaze and starts the deamon thread)
    def create_checkBox(App):
        App.exit_event = threading.Event()
        App.preSubmit_Thread = threading.Thread(target=App.check_numb_Bttns, name='preSubmition',daemon=True, args=())
        App.preSubmit_Thread.setDaemon(True)
        
        App.checkButtonList = []
        App.checkBttnVarList = []
        App.checkButton_SpecialList = []
        App.checkBttn_SpecialVar_List = []
        
        #frame A
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

            App.checkBttnVarList.append(IntVar())
            App.checkButtonList.append(Checkbutton(App.ticketFrameA, text=str(n+1), font=('Ubuntu'), variable=App.checkBttnVarList[n], onvalue=1, offvalue=0, height=3, width=2))
            
            App.checkButtonList[n].grid(row=r,column=c,padx=10, pady=15)
        
        #Frame B
        for m in range(15):
            if m>=0 and m<=9:
                r2=0
                c2=int(m)
            elif m>=10 and m<=15:
                r2=1
                c2=int(m%10)
    
            App.checkBttn_SpecialVar_List.append(IntVar())
            App.checkButton_SpecialList.append(Checkbutton(App.ticketFrameB, text=str(m+1), font=('Ubuntu'), variable=App.checkBttn_SpecialVar_List[m], onvalue=1, offvalue=0, height=3, width=2))

            App.checkButton_SpecialList[m].grid(row=r2, column=c2,padx=10,pady=15)
        
        #deamon thread that checks the numbers starts
        App.preSubmit_Thread.start()

    #Function to create the Buttons
    def create_Buttons(App):
        #Submition Button
        App.submit_Bttn = Button(App.mainWindow, text='Submit', command=App.submit)
        App.submit_Bttn.config(font=('Ubuntu'))
        App.submit_Bttn.pack(side=TOP, pady=5)

    #Daemon Thread Target that always checks the number of the selected numbers
    def check_numb_Bttns(App):
        App.finalSub = False
        
        while(True): # this loop the first time is not working well
            if App.exit_event.is_set():
                print('Daemon Thread exits!MAIN WHILE')
                break
            
            App.pre_submit()
            
            if len(App.selected_numbers)==6:
                App.disable_checkBoxes()
            elif len(App.selected_numbers)<6:
                for b in App.checkButtonList:
                    try:
                        b.config(state=NORMAL)
                    except:
                        pass
            
            if App.specialNumb != None:
                App.disable_checkBoxes_Special()
            else: 
                for b in App.checkButton_SpecialList:
                    try:
                        b.config(state=NORMAL)
                    except:
                        pass

            
            


    #Function that saves on a list the selected numbers    
    def pre_submit(App): 
        App.selected_numbers = []
        App.specialNumb = None
        i=1 # max -> range(len(checkBttnVarList))
        for v in App.checkBttnVarList:
            if(v.get() == 1):
                App.selected_numbers.append(i)
            i+=1
        j=1 
        for n in App.checkBttn_SpecialVar_List:
            if n.get() == 1:
                App.specialNumb = j
            elif j>len(App.checkBttn_SpecialVar_List):
                App.specialNumb = None
            j+=1
        
    
    #Function that disables all the unanted checkBoxes
    def disable_checkBoxes(App):
        i=0
        for b in App.checkButtonList:
            if App.exit_event.is_set():
                print('Daemon Thread exits! disable checkboxes')
                break
            if App.checkBttnVarList[i].get() == 0:
                try:
                    b.config(state=DISABLED) # in the meantime if the submit is at the same time as the disable
                except:                      # the buttons ca not be found so we throw an exception and pass the error 
                    pass
            i+=1
        
    #Function that disables all the unwanted checkBoxes from joker
    def disable_checkBoxes_Special(App):
        j=0
        for n in App.checkButton_SpecialList:
            if App.exit_event.is_set():
                print('Daemon Thread exits! disable special checkboxes')
                break
            if App.checkBttn_SpecialVar_List[j].get() == 0:
                try:
                    n.config(state=DISABLED) # in the meantime if the submit is at the same time as the disable
                except:                      # the buttons ca not be found so we throw an exception and pass the error 
                    pass
            j+=1

    #Function that warns the final submition (pop)
    def submit(App):
        App.message.config(text='')
        App.message_Frame.pack_forget()
        
        if len(App.selected_numbers) == 6 and App.specialNumb != None:
            App.msgBox = messagebox.askquestion("Confirm","Final submition.\n"+(str(App.selected_numbers) +'['+str(App.specialNumb)+']')+"\nAre you sure?")  
            
            if App.msgBox == 'yes':
                
                App.finalSub = True
                App.exit_event.set()

                App.submition = App.selected_numbers
                App.sub_special = App.specialNumb
                App.save_Submition(App.specialNumb)

                if App.exit_event.is_set():
                    Results()

        elif len(App.selected_numbers) < 6 or App.specialNumb == None:
            App.message_Frame.pack(side=TOP)
            App.message.config(text='You cannot submit yet.')
            App.message.pack()
    
    #Saves the submition on a mysql database
    #TABLE: submitions
    def save_Submition(App, joker):
        mycursor = App.mydb.cursor()
        
        try:
            print("Creating table {}: ".format('submitions'))
            mycursor.execute("CREATE TABLE `submitions` (`position` VARCHAR(7), `number` VARCHAR(7))")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Submitions table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
        i=0
        print("SUBLIST: " + str(App.submition))
        for n in App.submition:
            sql = "INSERT INTO submitions (position, number) VALUES (%s, %s)"
            val = (str(i+1), str(n))
            mycursor.execute(sql, val)
            App.mydb.commit()
            print(mycursor.rowcount, "record " + str(i+1) + " inserted.")
            i+=1
        
        sql = "INSERT INTO submitions (position, number) VALUES (%s, %s)"
        val = (str(7), str(joker))
        mycursor.execute(sql, val)
        App.mydb.commit()
        print(mycursor.rowcount, "joker inserted.\n")

        #
        mycursor.execute("SELECT * FROM submitions")
        myresult = mycursor.fetchall()

        print(myresult) 
       

    
#A class about the results
class Results(App):
    
    def __init__(App):
        for widget in App.mainWindow.winfo_children():
            widget.destroy()
        
        App.results_title = Label(App.mainWindow, text='Results', font=('Ubuntu',25), padx=200)
        App.results_title.pack(side=TOP)
       
        #The drawn numbers are ... 
        App.drawn_numb_frame = LabelFrame(App.mainWindow, height=100, width=200, text='The drawn numbers', font=('Ubuntu',10), borderwidth=3, relief=RIDGE, padx=100)
        App.drawn_numb_frame.pack(side=TOP, pady=10) 
        App.drawn_numb_label = Label(App.drawn_numb_frame, font=('Ubuntu'))
        App.drawn_numb_label.pack(side=TOP)
        App.Drawn()
        
        #Your submition
        App.subm_frame = LabelFrame(App.mainWindow, height=100, width=200, text='Your submition', font=('Ubuntu',10), borderwidth=3, relief=RIDGE, padx=100)
        App.subm_frame.pack(side=TOP, pady=10) 
        App.subm_label = Label(App.subm_frame, font=('Ubuntu'))
        App.subm_label.pack(side=TOP)
        App.Print_Submition()
        
        #Hited Numbers
        App.hit_numbers_frame = LabelFrame(App.mainWindow, height=100, width=200, text='You Hit', font=('Ubuntu',10), borderwidth=3, relief=RIDGE, padx=100)
        App.hit_numbers_frame.pack(side=TOP, pady=10) 
        App.hit_numbers_label = Label(App.hit_numbers_frame, font=('Ubuntu'))
        App.hit_numbers_label.pack(side=TOP)

        #Total Hits
        App.total_hits_frame = LabelFrame(App.mainWindow, height=100, width=200, text='Total Hits', font=('Ubuntu',10), borderwidth=3, relief=RIDGE, padx=100)
        App.total_hits_frame.pack(side=TOP, pady=10) 
        App.total_hits_label = Label(App.total_hits_frame, font=('Ubuntu'))
        App.total_hits_label.pack(side=TOP)
        
        #Success Rate
        App.success_rate_frame = LabelFrame(App.mainWindow, height=100, width=200, text='Success Rate', font=('Ubuntu',10), borderwidth=3, relief=RIDGE, padx=85)
        App.success_rate_frame.pack(side=TOP, pady=10) 
        App.success_rate_label = Label(App.success_rate_frame, font=('Ubuntu'))
        App.success_rate_label.pack(side=TOP)
        

        App.Display_Muched_Numbers()

    #Draw 7 numbers and print them   
    def Drawn(App):
        App.drawn_Numb = [] 
        # Draw 6 normal numbers 
        for i in range(6):
            n = random.randint(1,40)
            while n in App.drawn_Numb:
                n = random.randint(1,40)
            
            App.drawn_Numb.append(n)
        
        App.drawn_Numb.sort() # sort the List ascenting
        
        #Draw one special/Joker Number
        App.drawn_spNumb = random.randint(1,15)
        App.drawn_numb_label.config(text=str(App.drawn_Numb)+" ["+str(App.drawn_spNumb)+"]" , padx=2, pady=10, font=('Ubuntu',15))
    
    # Print the Submition Numbers
    def Print_Submition(App):
        mycursor = App.mydb.cursor()
        App.mySubmition = []
        mycursor.execute("SELECT number FROM submitions")
        myresult = mycursor.fetchall()
        
        #makes them from tuple to integer
        for n in myresult:
            res = int(''.join(map(str, n)))
            App.mySubmition.append(res)

        App.myjoker = App.mySubmition[6] # saves the joker
        App.mySubmition.pop(6) # and deletes the joker from the main numbers
        
        App.subm_label.config(text= str(App.mySubmition) +" ["+ str(App.myjoker)+"]", padx=2, pady=10, font=('Ubuntu',15))

    # Function that displays the muched numbers 
    def Display_Muched_Numbers(App):
        #Calculations
        App.hit_numbers = []
        App.total_hits = 0
        App.hited_joker = FALSE
        for s in App.mySubmition:
            for d in App.drawn_Numb:
                if s == d:
                    App.hit_numbers.append(s)
                    App.total_hits += 1
        if App.drawn_spNumb == App.myjoker:
            App.hited_joker = TRUE
            App.total_hits += 1
        App.success_rate = round((App.total_hits/7)*100)

        #Display
        #Total Hits
        if App.hited_joker == TRUE:
            App.total_hits_label.config(text= str(App.total_hits) + ", Hit Joker", padx=2, pady=10)
        else:
            App.total_hits_label.config(text= str(App.total_hits), padx=2, pady=10)            

        #Hited Numbers
        if App.hit_numbers == NONE:
            App.hit_numbers_label.config(text= "Nothing", padx=2, pady=10)
        else:
            App.hit_numbers_label.config(text= str(App.hit_numbers), padx=2, pady=10)

        #Succcess_rate
        App.success_rate_label.config(text= str(App.success_rate)+"%", padx=2, pady=10)

#MAIN RUN PROGRAM
app = App()


atexit.register(app.del_submition)
