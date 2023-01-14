#code UpdateGameBoard
#figure out where to implement while loop for detecting click
#we got IntBoard to update

import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import functools
import socket
#from clientPlayer1 import sendMove
from clientPlayer1 import connectionSocket

IntBoard = {}
count = 1
column = 1
isClicked = False



#Create dictionary of Internal TTT Board
for x in range(1,10):
    if count == 4:
        column += 1
        count = 1
        IntBoard[count, column] = 0
        count += 1
    else:
        IntBoard[count, column] = 0
        count += 1



class BoardClass:
    __player1name__ = 'Player1'
    __player2name__ = 'Player2'
    __lastplayer__ = 0
    __numberGames__ = 0

    def __init__(self, playerNum):
        self.__player1name__ = 'Player1'
        self.__player2name__ = 'Player2'
        self.__lastplayer__ = None
        self.__numberWins__ = 0
        self.__numberTies__ = 0
        self.__numberLoss__ = 0
        #call BoardGame UI here
        #self.UI = BoardUI(playerNum)


    def updateGamesPlayed(self):
        """Track how many games have been started."""
        return self.__numberGames__

    def resetGameBoard(self):
        """Clear game board."""
        self.__numberGames__ += 1
        pass

    def updateGameBoard(self):
        """Update board with player's move."""
        #oh call this when opponent sends their move
        pass

    def isWinner(self):
        """Check if last move is win and update win/loss count."""
        #within exterior while loop, keep running this to check whether winner is found
        #if (j, i) all 3 boxes start w/ same j/i and are occupied by same person
        #if (j, i) all 3 boxes where (j, i),(j+1, i+1),(j+2,i+2) or (j, i),(j-1,i+1),(j-2,i+2)
        player_list = []
        for Taken in (box for box in IntBoard if IntBoard[box] == 1):
            player_list.append(Taken)
        print(player_list)
        count = 0
        #for box in player_list:
            
            
        self.__numberWins__ += 1
        self.__numberGames__ += 1
        return self.__numberWins__

    def boardIsFull(self):
        """Check if board is full and update ties count."""
        self.__numberGames__ += 1
        self.__numberTies__ += 1
        pass

    def printStats(self):
        """Print 6 stats, each on new line."""
        pass

    def makeMove(self):
        """Detect user has made move."""
        global isClicked
        print('isClicked = {}'.format(isClicked))
        if isClicked == True:
            #isClicked = False
            print('isClicked is now = {}'.format(isClicked))
            return 'Move Made'
        else:
            return 'Wait for Move'
            
    def playGame(self):
        pass
        



class BoardUI():
    myBoard = 0
    master = 0
    name1 = 'Player1'
    name2 = 'Player2'
    player = '1'
    playerNum = 0
    buttons = []
    
    def __init__(self, playerNum):
        self.myBoard = BoardClass(playerNum)
        self.canvasSetup()
        self.entryName1()
        self.entryName2()
        self.createBoard()
        self.playerNum = playerNum
        self.displayPlayerName()
        self.quitButton()
        self.displayStats()
        self.myMove = 0
        self.runUI()
        #self.ReplayTextbox()
        #self.connsocket = connsocket

    def initTKVar(self):
        self.name1 = tk.StringVar()
        self.name2 = tk.StringVar()

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title('Tic Tac Toe')
        self.master.geometry('600x600')
        self.master.resizable(0, 0)

    def createBoard(self):
        self.button1 = tk.Button(self.master, text = "   ", command= lambda: self.click(1))
        self.buttons.append(self.button1)
        self.button1.grid(row="3", column="1", ipadx="40", ipady="30")
        self.button2 = tk.Button(self.master, text = "   ", command= lambda: self.click(2))
        self.buttons.append(self.button2)
        self.button2.grid(row="3", column="2", ipadx="40", ipady="30")
        self.button3 = tk.Button(self.master, text = "   ", command= lambda: self.click(3))
        self.buttons.append(self.button3)
        self.button3.grid(row="3", column="3", ipadx="40", ipady="30")
        self.button4 = tk.Button(self.master, text = "   ", command= lambda: self.click(4))
        self.buttons.append(self.button4)
        self.button4.grid(row="4", column="1", ipadx="40", ipady="30")
        self.button5 = tk.Button(self.master, text = "   ", command= lambda: self.click(5))
        self.buttons.append(self.button5)
        self.button5.grid(row="4", column="2", ipadx="40", ipady="30")
        self.button6 = tk.Button(self.master, text = "   ", command= lambda: self.click(6))
        self.buttons.append(self.button6)
        self.button6.grid(row="4", column="3", ipadx="40", ipady="30")
        self.button7 = tk.Button(self.master, text = "   ", command= lambda: self.click(7))
        self.buttons.append(self.button7)
        self.button7.grid(row="5", column="1", ipadx="40", ipady="30")
        self.button8 = tk.Button(self.master, text = "   ", command= lambda: self.click(8))
        self.buttons.append(self.button8)
        self.button8.grid(row="5", column="2", ipadx="40", ipady="30")
        self.button9 = tk.Button(self.master, text = "   ", command= lambda:[self.switch(9), self.trigger()])
        self.buttons.append(self.button9)
        self.button9.grid(row="5", column="3", ipadx="40", ipady="30")
##        self.button10 = tk.Button(self.master, text = "   ", default)
##        self.button10.grid(row="6", column="1", ipadx="40", ipady="30")

    def switch(self, boxNum):
        listIndex = int(boxNum - 1)
        self.buttons[listIndex].config(text='x')
        self.buttons[listIndex]["state"] = tk.DISABLED

        return boxNum


    def enable(self):
        for button in self.buttons:
            button["state"] = tk.NORMAL
        print('went into enable func')


    def disable(self):
        for button in self.buttons:
            button["state"] = tk.DISABLED

    def click(self, boxNum):
        global isClicked
        global IntBoard
        if self.playerNum == '1':
            listIndex = int(boxNum - 1)
            self.buttons[listIndex].config(text='x')
            #sendMsg on socket
            if boxNum % 3 == 0:
                IntBoard[3, int(boxNum / 3)] = 1
            else:
                IntBoard[boxNum % 3, math.ceil(boxNum/3)] = 1
            print(IntBoard)
        elif self.playerNum == '2':
            listIndex = int(boxNum - 1)
            self.buttons[listIndex].config(text='o')
            if boxNum % 3 == 0:
                IntBoard[int(boxNum / 3), math.ceil(boxNum/3)] = 2
            else:
                IntBoard[boxNum % 3, math.ceil(boxNum/3)] = 2
        isClicked = True
        self.myMove = boxNum
        print('This is connectionSocket in gameboard: ', connectionSocket)
        #self.sendMove(boxNum)
        
    def sendMove(self,move):
        print('Entered sendMove Function')
        return move

        #global connectionSocket
##        connectionSocket.send(bytes(my_username, 'utf-8'))
##        #wait to receive player 2's username
##        serverData = connectionSocket.recv(10)        
##        print(serverData.decode('ascii'))
        
        self.myBoard.makeMove()
        #return ('Click')

    def makeMove(self):
        """Allow user select their move by clicking."""
        pass

    def ReplayTextbox(self):
        #Make sure this only pops up for Player 1
        #self.replay = tk.messagebox.askquestion(title="ReplayGame", message="Would you like to play again?")
        self.replay = tk.simpledialog.askstring("Continue game", "Would you like to play again?")
        if self.replay == "y" or self.replay == "Y":
            #send "Play Again" to player 2
            pass
        elif self.replay == "n" or self.replay == "N":
            #send"Fun Times to player 2"
            #Player 2 prints statistics
            pass



    def displayStats(self):
        #Player 2 will be calling this
        """Display area of reporting statistics when finished playing."""
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=8, column=0)

        self.title = tk.Label(self.frame, text="Game Statistics")
        self.stat1 = tk.Label(self.frame, text="Username:", anchor=tk.W)
        self.stat2 = tk.Label(self.frame, text="Last to Move:")
        self.stat3 = tk.Label(self.frame, text="Number Games Played:")
        self.stat4 = tk.Label(self.frame, text="Number of Wins:")
        self.stat5 = tk.Label(self.frame, text="Number of Losses:")
        self.stat6 = tk.Label(self.frame, text="Number of Ties:")
        self.title.grid(row=8, column=0)
        self.stat1.grid(row=9, column=0)
        self.stat2.grid(row=10, column=0)
        self.stat3.grid(row=11, column=0)
        self.stat4.grid(row=12, column=0)
        self.stat5.grid(row=13, column=0)
        self.stat6.grid(row=14, column=0)

    def entryName1(self):
        self.preview1 = tk.Label(self.master, text='Player 1 Username')
        self.preview1.grid(row=1, column=0)
        self.textbox = tk.Text(self.master, height = 1, width = 10)
        self.textbox.grid(row=1, column=1, columnspan = 8)
        self.buttonEnter = tk.Button(self.master, height=1, width=10, text="Enter", command=lambda: self.getName(self.textbox))
        self.buttonEnter.grid(row=1, column=3, columnspan = 4)

    def getName(self, textbox):
        self.inputValue = textbox.get("1.0", "end")
        #send self.inputValue to player 2
        #wait to receive player 2's username
        print(self.inputValue)
        return self.inputValue

    def entryName2(self):
        self.preview2 = tk.Label(self.master, text='Player 2 Username')
        self.preview2.grid(row=2, column=0)
        self.textbox2 = tk.Label(self.master, text='player2')
        self.textbox2.grid(row=2, column=1, columnspan = 8)


    def displayPlayerName(self):
        """Area displaying user name of current players turn."""
        self.display = tk.Label(self.master, text='Player{}\'s turn; What is your move?'.format(self.playerNum))
        self.display.grid(row=6, column=1, columnspan=8)


    def quitButton(self):
        """Quit button that allows user to quit before finishing game. Close client UI and end program."""
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quitButton.grid(row="7", column="2")

    def runUI(self):
        """Enable UI to start."""
        self.master.mainloop()

if __name__ == "__main__":
    myboard = BoardClass('1')
    myUI = BoardUI('1')


    #myUI.trigger.has_been_called = False
    #myUI.enable()
    
    
#Add your ip/tcp socket below
##    while (1):
##        if (isClicked == True):
##            isClicked = False
            # do what you want such as check winer or board is full ...
        # check whether receive message from opponent .. update game GUI board and IntBoard

    
    #myboard = BoardUI('1')
