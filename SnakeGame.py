"""
This program is just a block style of snake. It was made for fun using the tkinter
class.

Porter Dalton
12/29/2019
"""
from tkinter import *
from functools import partial
from PIL import Image
from random import choice


class Snake:
    """This is where the snake game is set up and starts playing"""

    def __init__(self, master, *args):
        """Initializer where the game is set up and drawn"""
        self.master = master
        h = args[0] #Height of the gameboard args[0]
        w = args[1] #Width of the gameboard args[1]
        padC = 3 #bigger the number, smaller the squares
        bugPadC = 17
        self.x = 0
        self.y = 0
        self.direction = "right" #Establishes the first direction the sake faces
        self.snakeLength = args[2] #How long the initial snake is
        self.should_continue = True #If this is false the loop ends and so does the game

        #Initial canvas where everthing is drawn
        self.c = Canvas(self.master, bg = "black", height = h * 50, width = w * 50)
        self.grid = {}
        self.bugs = {}
        self.snakeItems = []

        #Create all the shapes for the snake and the potential coordinates for the bugs
        for x in range(0, w * 50, 50):
            for y in range(0, h * 50, 50):
                self.bugs[(x // 50,y // 50)] = (x+bugPadC,y+bugPadC,x+50-bugPadC,y+50-bugPadC)
                self.grid[(x // 50,y // 50)] = self.c.create_rectangle(x+padC,y+padC,x+50-padC,y+50-padC, fill = "black")
        self.c.pack()

        #Possible keyboard inputs
        self.moveFrame = Frame(master, width=0, height = 0)
        self.moveFrame.bind("<Down>", partial(self.changeDirection, "down"))
        self.moveFrame.bind("<Up>", partial(self.changeDirection, "up"))
        self.moveFrame.bind("<Left>", partial(self.changeDirection, "left"))
        self.moveFrame.bind("<Right>", partial(self.changeDirection, "right"))
        self.moveFrame.bind("<Key>", self.addLength)
        self.moveFrame.pack()
        self.moveFrame.focus_set()

        #Snake is given a place to start
        self.c.itemconfigure(self.grid[(0, 0)], fill = "white")
        self.snakeItems.insert(0,(0,0))
        
        #Add the first bug
        self.addBug()

        #Start
        self.startCycles()

    
    def oneCycle(self, direct):
        """Checks to see if the direction has changed or if the snake has hit anything
        Also adds one space to the snake"""

        if (direct == "down"):
            try:
                self.grid[(self.x, self.y+1)]
            except KeyError:
                self.endGame()
            else:
                self.c.itemconfigure(self.grid[(self.x,self.y + 1)], fill = "white")
                self.y += 1

        if (direct == "up"):
            try:
                self.grid[(self.x, self.y-1)]
            except KeyError:
                self.endGame()
            else:
                self.c.itemconfigure(self.grid[(self.x,self.y - 1)], fill = "white")
                self.y -= 1

        if (direct == "left"):
            try:
                self.grid[(self.x-1, self.y)]
            except KeyError:
                self.endGame()
            else:
                self.c.itemconfigure(self.grid[(self.x - 1,self.y)], fill = "white")
                self.x -= 1

        if (direct == "right"):
            try:
                self.grid[(self.x+1, self.y)]
            except KeyError:
                self.endGame()
            else:
                self.c.itemconfigure(self.grid[(self.x + 1,self.y)], fill = "white")
                self.x += 1
                
        if ((self.x, self.y) in self.snakeItems): #If snake hits itself
            self.endGame()
        else:
            self.snakeItems.insert(0, (self.x, self.y))
            if (self.bugLoc == (self.x, self.y)):
                self.eatBug()

        if (self.snakeLength == len(self.snakeItems)-1):
            self.c.itemconfigure(self.grid[self.snakeItems.pop()], fill = "black")


    def startCycles(self):
        """Starts the loop for the game"""
        if (self.should_continue):
            self.oneCycle(self.direction)
            self.stop = self.master.after(150, self.startCycles)


    def changeDirection(self, dyrec, m = 1):
        """takes a direction and makes sure the direction isn't a 180"""
        #All these if statements are to make sure the snake doesn't make a 180
        if ((dyrec == "right" and self.direction != "left") or
            (dyrec == "left" and self.direction != "right") or
            (dyrec == "up" and self.direction != "down") or
            (dyrec == "down" and self.direction != "up")):

            self.direction = dyrec
    
    def addLength(self):
        """Add 1 length to the snake"""
        self.snakeLength += 1

    def addBug(self):
        """Adds a single bug somewhere randomly on the board as long as it isn't on the snake"""
        while(True):
            self.bugLoc = choice(list(self.bugs.keys())) #Location of the bug
            if not self.bugLoc in self.snakeItems:
                a = self.bugs[(self.bugLoc)][0]
                b = self.bugs[(self.bugLoc)][1]
                c = self.bugs[(self.bugLoc)][2]
                d = self.bugs[(self.bugLoc)][3]
                self.newBug = self.c.create_rectangle(a, b, c, d, fill = "green")
                break

    def eatBug(self):
        self.c.delete(self.newBug)
        self.addLength()
        self.addBug()

    def endGame(self):
        """Ends the game, stops the loop and makes the head of the snake turn red"""
        self.should_continue = False
        self.master.after_cancel(self.stop)
        self.c.itemconfigure(self.grid[self.snakeItems[0]], fill = "red")

    

def main():
    """main function, just creates a tkinter window and puts it in the snake game"""
    root = Tk()
    #           H   W   SnakeLength
    Snake(root, 14, 20, 7)
    root.mainloop()

if __name__ == "__main__":
    main()