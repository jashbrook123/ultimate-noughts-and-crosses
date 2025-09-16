import tkinter as tk
import math
from tkinter import Y, messagebox
import numpy as np

grid = np.full((9, 9), " ") # the 9x9 grid seen by players
ultimateGrid = np.full((3, 3), " ") # the ultimate game
drawCounter = 0

def win(winner):
    global drawCounter,xCount,oCount,grid, ultimateGrid
    if winner == "x": xCount +=1
    elif winner == "o": oCount +=1
    tk.messagebox.showinfo(title="The winner is...", message=f"{winner} has won")  
    game.delete("all")
    grid = np.full((9, 9), " ") # the 9x9 grid seen by players
    ultimateGrid = np.full((3, 3), " ") # the ultimate game
    createBoard()
    drawCounter = 0
    
    
def completeSquare(range1,range2):
    for x in range(range1,range1+3):
        for y in range(range2,range2+3):
            grid[y,x]= "B"

def draw():
    global drawCounter,grid, ultimateGrid
    tk.messagebox.showinfo(title="The winner is...", message=f"There was a draw!")  
    game.delete("all")
    grid = np.full((9, 9), " ") # the 9x9 grid seen by players
    ultimateGrid = np.full((3, 3), " ") # the ultimate game
    createBoard()
    drawCounter = 0

def ultimateGridUpdate(x,y,winner): # adds the winner of the smaller 3x3 in to a variable to keep track of the big 3x3
    global ultimateGrid, drawCounter
    ultimateGrid[y,x] = winner
    drawCounter +=1
    ultimateGridCheck()

def ultimateGridCheck(): # checks win condition for the ultimate grid
    winner = ""
    if len(set(ultimateGrid[0])) == 1 and ultimateGrid[0,0] != " ": winner = ultimateGrid[0,0]
    elif len(set(ultimateGrid[1])) == 1 and ultimateGrid[1,0] != " ": winner = ultimateGrid[1,0]
    elif len(set(ultimateGrid[2])) == 1 and ultimateGrid[2,0] != " ": winner = ultimateGrid[2,0]
    elif ultimateGrid[0,0] == ultimateGrid[1,0] and ultimateGrid[1,0] == ultimateGrid[2,0] and ultimateGrid[0,0] != " " : winner = ultimateGrid[0,0] 
    elif ultimateGrid[0,1] == ultimateGrid[1,1] and ultimateGrid[1,1] == ultimateGrid[2,1] and ultimateGrid[0,1] != " " : winner = ultimateGrid[0,1] 
    elif ultimateGrid[0,2] == ultimateGrid[1,2] and ultimateGrid[1,2] == ultimateGrid[2,2] and ultimateGrid[0,2] != " " : winner = ultimateGrid[0,2] 
    elif ultimateGrid[0,0] == ultimateGrid[1,1] and ultimateGrid[1,1] == ultimateGrid[2,2] and ultimateGrid[0,0] != " " : winner = ultimateGrid[0,0] 
    elif ultimateGrid[0,2] == ultimateGrid[1,1] and ultimateGrid[1,1] == ultimateGrid[2,0] and ultimateGrid[2,0] != " " : winner = ultimateGrid[2,0]   
    if winner != "":win(winner)
    if drawCounter == 9:
        draw()

def createBoard(): # Creates a 9x9 grid
    x1,y1,x2,y2 = 0,100,0,1000
    while x1 < 1000:
        x1+=100
        x2+=100
        if (x1-100)%3==0:
            game.create_line(x1,y1,x2,y2,width=5,fill="skyblue1")
        else:
            game.create_line(x1,y1,x2,y2,width=5)
    x1,y1,x2,y2 = 100,0,1000,0
    while y1 < 1000:
        y1+=100
        y2+=100
        if (y1-100)%3==0:
            game.create_line(x1,y1,x2,y2,width=5,fill="skyblue1")
        else:
            game.create_line(x1,y1,x2,y2,width=5)

def switchTurn(): # switches turn between players
    global playerTurn,player1,player2
    
    if playerTurn == 1:
        playerTurn=2
        player1.destroy()
        player2.destroy()
        player1 = tk.Label(game, text = f"Player X ({xCount})", font = ("Arial",12 ), bg="Red")
        player2=tk.Label(game,text=f"Player O ({oCount})", font = ("Arial",12 ), bg="Blue",fg="white")
        player1.place(x=500,y=20,anchor='n')
        player2.place(x=600,y=20,anchor='n')
    elif playerTurn == 2:
        playerTurn=1
        player1.destroy()
        player2.destroy()
        player1 = tk.Label(game, text = f"Player X ({xCount})", font = ("Arial",12 ), bg="Red",fg="white")
        player2=tk.Label(game,text=f"Player O ({oCount})", font = ("Arial",12 ), bg="Blue")
        player1.place(x=500,y=20,anchor='n')
        player2.place(x=600,y=20,anchor='n')

def gridAddX(pos): #Adding the x on the array
    x,y = displayMouse(pos.x,pos.y)
    y = int(str(y)[0])-1
    x = int(str(x)[0])-1
    grid[y,x] = "x"
        
def gridAddO(pos):
    x,y = displayMouse(pos.x,pos.y)
    y = int(str(y)[0])-1
    x = int(str(x)[0])-1
    grid[y,x] = "o"

def gridCheck(pos): #Checks whether something else in this position
    x,y = displayMouse(pos.x,pos.y)
    y = int(str(y)[0])-1
    x = int(str(x)[0])-1
    if grid[y,x] != " ":
        return False
    else:
        return True

def clickX(pos): #Places the x on the grid
    tempx,tempy = displayMouse(pos.x,pos.y) #returns the grid position of the mouse
    if gridCheck(pos):
        game.create_line(tempx-25,tempy-25,tempx+25,tempy+25,fill="red",width=5) #permenantely places the cross on that spot
        game.create_line(tempx+25,tempy-25,tempx-25,tempy+25,fill="red",width=5)
        gridAddX(pos)
        switchTurn()
    
def clickO(pos):
    global board
    tempx,tempy = displayMouse(pos.x,pos.y)
    if gridCheck(pos):
        game.create_oval(tempx-25,tempy-25,tempx+25,tempy+25,outline="blue",width=5)
        gridAddO(pos)
        switchTurn()

def displayO(x,y): #Deletes previous x and spawns a new one
    global circle1
    game.delete(circle1)
    circle1=game.create_oval(x-25,y-25,x+25,y+25,outline="blue",width=5)
    
def displayX(x,y): #Deletes previous x and spawns a new one
    global cross1,cross2
    game.delete(cross1)
    game.delete(cross2)   
    cross1=game.create_line(x-25,y-25,x+25,y+25,fill="red",width=5)
    cross2=game.create_line(x+25,y-25,x-25,y+25,fill="red",width=5)          
        
def displayMouse(x,y): #Finds the square that the cursor is in
    global playerTurn
    tempx=0
    tempy=0
    change = False
    x = ((math.ceil(x/100))*100) - 50
    y = ((math.ceil(y/100))*100) - 50
    if tempx==0:
        tempx=x
        tempy=y
        change = True
    if x != tempx:
        tempx=x
        change = True
    if y!= tempy:
        tempy=x
        change = True
    if change == True:
        if playerTurn == 1:
            displayX(tempx,tempy)
        elif playerTurn == 2:
            displayO(tempx,tempy)
    return tempx,tempy
    
def callback(e): #Finds the mouse position at all times (e = info on mouse position)
    x= e.x
    y= e.y
    if x > 100 and x < 1000 and y > 100 and y < 1000:
        displayMouse(x,y) 

def click(pos): #run when left clicked, and runs the function for placing the object
    global playerTurn
    x = pos.x
    y = pos.y
    if x < 1000 and x > 100 and y < 1000 and y > 100:
        if playerTurn == 1:
            clickX(pos)
        elif playerTurn == 2:
            clickO(pos)
        smallWin()

def loopCheckHorizontal(range1,range2):# checks for horizontal lines and can loop through a number of times
    for x in range(0,9):
        gridList = []
        for y in range(range1,range2):
            gridList.append(grid[x,y])
        if len(set(gridList)) == 1 and gridList[0] != " ":
            winner = str(gridList[0])
            if winner == "x":
                smallWinX(y,x)
            elif winner == "o":
                smallWinO(y,x)

def loopCheckVertical(range1,range2):# checks for horizontal lines and can loop through a number of times
    for y in range(0,9):
        gridList = []
        for x in range(range1,range2):
            gridList.append(grid[x,y])
        if len(set(gridList)) == 1 and gridList[0] != " ":
            winner = str(gridList[0])
            if winner == "x":
                smallWinX(y,x)
            elif winner == "o":
                smallWinO(y,x)

def loopCheckDiagonalLR(range1,range2): #checks the diagonal lines from top left to bottom right
    y=0
    while y <9:
        gridList = []
        for x in range(range1,range2):
            gridList.append(grid[x,y])
            y+=1
        if len(set(gridList)) == 1 and gridList[0] != " ":
            winner = str(gridList[0])
            if winner == "x":
                smallWinX(y-1,x)
            elif winner == "o":
                smallWinO(y-1,x)

def loopCheckDiagonalRL(range1,range2): #checks the diagonal lines from top right to bottom left
    loopNumber = 0
    while loopNumber < 9:    
        gridList = []
        maxRange = range2-1
        for x in range(range1,range2):
            y = maxRange - x + loopNumber
            gridList.append(grid[x,y]) #ends loop with the top right coordinate y,x
        x=x-2
        if len(set(gridList)) == 1 and gridList[0] != " " and gridList[0] != "B":
            winner = str(gridList[0])
            if winner == "x":
                smallWinX(y,x)
            elif winner == "o":
                smallWinO(y,x)
        loopNumber+=3
    
        
def smallWin(): # holds code for calling loops in order to check each area
    range1,range2=0,3 ## this checks all horizontal lines
    while range2 < 10:
        loopCheckHorizontal(range1,range2)
        range1+=3
        range2+=3
    range1,range2=0,3 ## this checks all vertical lines
    while range2 < 10:
        loopCheckVertical(range1,range2)
        range1+=3
        range2+=3
    range1,range2=0,3
    while range2 < 10:
        loopCheckDiagonalLR(range1,range2)
        range1+=3
        range2+=3
    range1,range2=0,3
    while range2 < 10:
        loopCheckDiagonalRL(range1,range2)
        range1+=3
        range2+=3

def smallWinX(x,y): # places a cross over the 3x3 section and adds to the ultimateGrid
    x,y = roundCoords(x,y)
    completeSquare((x-100)//100,(y-100)//100)
    gridX,gridY = roundGridCoordinates((x-100)//100,(y-100)//100)
    game.create_line(x+5,y+5,x+295,y+295,fill="pink",width=5)
    game.create_line(x+295,y+5,x+5,y+295,fill="pink",width=5)
    ultimateGridUpdate(gridX,gridY,"x")

def smallWinO(x,y):
    x,y = roundCoords(x,y)
    completeSquare((x-100)//100,(y-100)//100)
    gridX,gridY = roundGridCoordinates((x-100)//100,(y-100)//100)
    game.create_oval(x+5,y+5,x+295,y+295,outline="purple",width=5)
    ultimateGridUpdate(gridX,gridY,"o")

def roundCoords(x,y): # takes the coordinates and transforms them into the coordinate of the lop left spot of that 3x3 grid
    if x < 3: x = 100
    elif x < 6: x = 400
    elif x < 9: x = 700
    if y < 3: y = 100
    elif y < 6: y = 400
    elif y < 9: y = 700
    return x,y

def roundGridCoordinates(gridX,gridY): # gives a coordinate realtive to the ultimate 3x3
    if gridX == 3: gridX = 1
    elif gridX == 6: gridX = 2
    if gridY == 3: gridY = 1
    elif gridY == 6: gridY = 2
    return gridX,gridY

root = tk.Tk() # root screen
root.geometry("1100x1100")
root.configure(bg="green")

game = tk.Canvas(root, width=1100,height=1100,bg="green") # canvas for the game 
game.pack()
xCount,oCount,playerTurn = 0,0,2 # Turn 1 = X Turn 2 = O
    
boardY0,boardY1,boardY2 = list(["","",""]),list(["","",""]),list(["","",""])
cross1,cross2,circle1=game.create_line(0,0,0,0,fill="red",width=0),game.create_line(0,0,0,0,fill="red",width=0),game.create_oval(0,0,0,0,fill="blue",width=5)

player1 = tk.Label(game, text = f"Player X ({xCount})", font = ("Arial",12 ), bg="Red")
player2=tk.Label(game,text=f"Player O ({oCount})", font = ("Arial",12 ), bg="Blue")
player1.place(x=550,y=20,anchor='n')
player2.place(x=300,y=20,anchor='n')

createBoard()
switchTurn()

game.bind("<Button-1>",click) # listening for mouse click
game.bind("<Motion>",callback) # listening for mouse movement

# current bugs = RL diag not working-coordinate system for that function not working

game.mainloop()
