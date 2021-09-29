import random
import time
from tkinter.constants import TRUE

class Lottery:
    #Take the inputs of the user
    def Inputs(self):
        numbSelec = []
        found = 0
        print("Type 6 numbers between 1 and 40.")
        for i in range (6):
            while True:
                if i > 0:
                    print("You have selected the following numbers: "+ str(numbSelec))
                    if i > 6:
                        print("Type "+str(6-i)+" numbers between 1 and 40.")
                    else:
                        print("Type "+str(6-i)+" number between 1 and 40.")
                inp = int(input())
                if inp <= 40 and inp >= 1:
                    for n in numbSelec: 
                        if inp == n:
                            found = 1
                            break
                        else:
                            found = 0 
                    if found == 0:
                        numbSelec.append(inp)
                        break
                    else:
                        print("\nThis number has already been selected\n")
                        
                else:
                    print("\nThis number does not meet the criteria. Try again...\n")                 
        
        while True:
            print("\nYou have selected the following numbers: "+ str(numbSelec))
            print("Now type 1 number between 1 and 15.")
            inp = int(input())
            if inp <= 15 and inp >= 1:
                for n in numbSelec: 
                    if inp == n:
                        found = 1
                        break
                    else:
                        found = 0 
                if found == 0:
                    numbSelec.append(inp)
                    break
                else:
                    print("\nThis number has already been selected\n")
                    
            else:
                print("\nThis number does not meet the criteria. Try again...\n")
    
                    
        return numbSelec

    #Start the Lottery and returns the random numbers
    def Lottery(self):
        randNumb = []
        
        for i in range (6):
            if i == 0:
                print("The first number is... ")
                #time.sleep(random.randint(1,3))
            else:
                print("And the next number is... ")
                #time.sleep(random.randint(1,3))

            #random 6 numbers between 1 and 40
            randNumb.append(random.randint(1, 40))
            print(randNumb[i])
            
            #time.sleep(random.randint(2,3))

        #the 7th random number between 1 and 15
        print("The last number is... ")
        #time.sleep(random.randint(1,3))
        
        randNumb.append(random.randint(1,15))
        
        
        print(randNumb[6])
        #time.sleep(random.randint(2,3))

        return randNumb

    def Results(self, selecNumb, randNumb):
        count = int(0)
        j=1
        for i in selecNumb :
            if(i == randNumb[j]):
                if(j == 1):
                    print("You hit the " + str(j) +"st Number: " +str(i))
                elif(i == 2):
                    print("You hit the " + str(j) +"nd Number: " +str(i))
                elif(i == 3):
                    print("You hit the " + str(j) +"rd Number: " +str(i))
                elif(i == 7):
                    print("You hit the last Number: " +str(i)) 
                else:
                    print("You hit the " + str(j) +"th Number: " +str(i))
                count=count+1
            j = j+1   
        print("\nYou hit in total " + str(count) + " from "+ str(j-1) +" numbers")
            
        percent = count/(j)
        print("\nYou achieved " + str(percent) +"%")


    def Main(self):
        selecNumb = self.Inputs()
        randNumb = self.Lottery()
        self.Results(selecNumb, randNumb)

##MAIN##
app = Lottery()
app.Main()