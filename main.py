from tkinter import *
from functools import partial


class mainWindow:
    def __init__(self, master):
        self.master = master
        h = 700
        w = 1000
        padC = 3
        self.x = 0
        self.y = 0
        self.direction = "right"
        self.snakeLength = 5

        self.c = Canvas(self.master, bg = "black", height = h, width = w)
        self.grid = {}
        self.snakeItems = []
        for x in range(0, w, 50):
            for y in range(0, h, 50):
                self.grid[(x / 50,y / 50)] = self.c.create_rectangle(x+padC,y+padC,x+50-padC,y+50-padC, fill = "black")

        self.c.pack()

        self.moveFrame = Frame(master, width=0, height = 0)
        self.moveFrame.bind("<Down>", partial(self.changeDirection, "down"))
        self.moveFrame.bind("<Up>", partial(self.changeDirection, "up"))
        self.moveFrame.bind("<Left>", partial(self.changeDirection, "left"))
        self.moveFrame.bind("<Right>", partial(self.changeDirection, "right"))
        self.moveFrame.bind("<Key>", self.addLength)
        self.moveFrame.pack()
        self.moveFrame.focus_set()

        self.c.itemconfigure(self.grid[(0, 0)], fill = "white")
        self.snakeItems.insert(0,(0,0))

        self.startCycles()

        gridArray = {}
    
    def oneCycle(self, direct):
        if (direct == "down" and self.direction != "up"):
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

        self.snakeItems.insert(0, (self.x, self.y))

        if (self.snakeLength == len(self.snakeItems)-1):
            self.c.itemconfigure(self.grid[self.snakeItems.pop()], fill = "black")


    def startCycles(self):
        self.oneCycle(self.direction)
        self.stop = self.master.after(200, self.startCycles)

    def changeDirection(self, dyrec, m = 1):
        if ((dyrec == "right" and self.direction != "left") or
            (dyrec == "left" and self.direction != "right") or
            (dyrec == "up" and self.direction != "down") or
            (dyrec == "down" and self.direction != "up")):

            self.direction = dyrec
    
    def addLength(self, event):
        if (event.char == " "):
            self.snakeLength += 1

    def endGame(self):
        self.master.after_cancel(self.stop)
        self.c.itemconfigure(self.grid[self.snakeItems[0]], fill = "red")

def main():
    root = Tk()
    mainWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()