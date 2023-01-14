import socket
import gameboard
import time
import threading
import asyncio
connectionSocket = 0


def establishConnect():
    while True:
        try:
            serverAddress = str(input('Enter host name or IP address of player 2'))
            serverPort = int(input('Enter port number'))
            global connectionSocket
            connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            f = connectionSocket.makefile()
            connectionSocket.connect((serverAddress,serverPort))
            #gameboard.BoardUI.connsocket = connectionSocket            
            return True

        except:
            
            answer = str(input('Do you want to try again?'))
##            if answer == 'y':
##                pass

            if answer == 'n':

                print('Closing the program')
                #add something to end entire thing? Or is this fine
                return False

        
def sendInfo():
    #global connectionSocket
    my_username = "Player 1 Username"
    connectionSocket.send(bytes(my_username, 'utf-8'))
    #wait to receive player 2's username
    serverData = connectionSocket.recv(10)
    print(serverData.decode('ascii'))

    #Import GUI here
    global player1
    global player1GUI
    player1 = gameboard.BoardClass('1')
    player1GUI = gameboard.BoardUI('1')
    #player1GUI.enable()
    print('Did we get to last line?')
    
##    while True:           
##        print("i am here2")        
##        await asyncio.sleep(3)
        
    #await asyncio.sleep(5)
    #closing the connection when I am done
    connectionSocket.close()

def sendMove(move):
    print('Entered sendMove Function')
    #print(connectionSocket)
    print(move)
    connectionSocket.send(bytes(str(move), 'utf-8'))
    #wait to receive player 2's username
    serverData = connectionSocket.recv(10)
    print(serverData.decode('ascii'))
    


if __name__ == "__main__":
    
    if establishConnect():
        contConnect = True
        print(connectionSocket)
        sendInfo()
        while contConnect == True:
            print('got inside while loop1')
            if gameboard.isClicked == True:
                    #get move and send
                    #1)either detect change in Int board
                    #2) or get move directly from GUI
                print('got inside clicked')
                    #print('From client ', move)
                break
                #FIXME: BRING NEXT 2 LINES BACK
##                move = player1GUI.myMove
##                connectionSocket.send(bytes(move, 'utf-8'))

                #wait to receive player 2's username
##            serverData = connectionSocket.recv(10)
##            print(serverData.decode('ascii'))
                gameboard.isClicked = False
            
##        tryConnect = establishConnect()
##    if tryConnect == True:
##        contConnect = True
##        print('did we get here?')
##        #GUI created here
##        sendInfo()
##        print('I do not think we got here')
##        while contConnect == True:
##            if gameboard.isClicked == True:
##                #get move and send
##                #1)either detect change in Int board
##                #2) or get move directly from GUI
##                print('got inside while loop')
##                #print('From client ', move)
##                connectionSocket.send(bytes('My move', 'utf-8'))
##                #wait to receive player 2's username
##                serverData = connectionSocket.recv(10)
##                print(serverData.decode('ascii'))
##                gameboard.isClicked = False


##    tryConnect = establishConnect()
##    while tryConnect == "Try Again":
##        tryConnect = establishConnect()
##    sendInfo()
    #time.sleep(5)
##    event = threading.Event()
    #event.wait(5)
##    contConnect = False

    
            
##    if tryConnect == True:
##        contConnect = True

        #FIXME: WE STOPPED HERE
##        print(gameboard.isClicked)
##        while gameboard.isClicked:
##            connectionSocket.send(bytes(my_username, 'utf-8'))
##            #wait to receive player 2's username
##            serverData = connectionSocket.recv(10)
##            print(serverData.decode('ascii'))
##            gameboard.isClicked = False
##            #user_move = input('What is your move?')
##            break
    
    
                
        
##        while contConnect:
##            if player1.makeMove == 'Move Made':
##                print('Move has been made')
##            else:
##                print('Keep waiting to make move')
##                break

##        while contConnect:
##            sendInfo()
##            
##            if player1.makeMove == 'Move Made':
##                print('Move has been made')
##            else:
##                print('Keep waiting to make move')
##                break
            

##    contConnect = establishConnect()
       
##    while (contConnect):
##        
##        if (gg.IsClicked):
##            gg.IsClicked = False
##            # do what you want such as check winer or board is full ..
##    
##            serverData = connectionSocket.recv(4)
##            if (board is full) or (there is winner):
##            break

