#This is a program to simulate roulette at a casino
import random

class Player(): #This is the player object class
   
    def __init__(self, name = "player", balance = 100):     #Creates a player, name and balance parameters
        self.__name = name
        self.__balance = balance
       
    def setName(self, name):        #Name Setter
        self.__name = name
   
    def setBalance(self, balance):
        self.__balance = balance
       
    def getName(self):
        return self.__name
   
    def getBalance(self):
        return self.__balance
   
    def getStr(self):
        print(self.__name + " (Balance = $" + str(self.__balance) + ")" )                    # Prints user name and user balance
       
    def winner(self, d):                                    # Updates balance with user bet when winning a comeout roll or hitting a point when comeOut = false
        self.__balance = self.__balance + d                 
        return self.__balance
   
    def loser(self, w):                                     # Updates balance with user bet when losing a comeout roll or 7-out when comeOut = false
        self.__balance = self.__balance - w
        return self.__balance


#Spin returns a number from -1 to 36, -1 being 00, and 0 being 0
def spin():
    x = random.randint(-1,36)
    return x

def single():
    nums = []
    keepbetting = 'y'
    while keepbetting == 'y':
        num = int(input('Enter the number you would like to bet on (-1 for 00)'))
        nums.append(num)
        keepbetting = input('Would you like to keep betting? y/n')
    return nums

    

        

def main():

    colorMap = {-1:'green', 0:'green',1:'red', 2:'black', 3:'red', 4:'black', 5:'red', 6:'black',
    7:"red", 8:'black', 9:'red', 10:'black', 11:'black', 12:'red', 13:'black', 14:'red', 15:'black',
    16:'red', 17:'black', 18:'red', 19:'black', 20:'black', 21:'red', 22:'black', 23:'red', 24:'black',
    25:'red', 26:'black', 27:'red', 28:'red', 29:'black', 30:'red', 31:'black', 32:'red', 33:'black', 34:'red', 35:'black', 36:'red'}

    name = input("What is your name? = ")                   #User input for name
    Player1 = Player(name, 100)                             #Creates Player object with given name parameter and 100 starting bankroll
    Player1.getStr()

    keepPlaying = 'yes'                                     # How I decided to control the main game loops below
   
    while keepPlaying == "yes" or keepPlaying == "y" or keepPlaying == "Y":             #Start of main loop, ends if player does not enter y
        if (Player1.getBalance() <= 1):                                                 #Ends main loop if player attempts to play with 0 dollars
            print("You ran out of money!")
            break
        x = spin()

        print(x,colorMap[x])
        keepPlaying = 'n'



#if __name__ == '__main__':
   # main()
