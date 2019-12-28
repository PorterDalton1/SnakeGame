from tkinter import *

class mainWindow:
    def __init__(self, master):
        self.master = master
        self.c = Canvas(self.master, bg = "black", height = 500, width = 500)
        pos1 = {"x":150, "y":50}
        pos2 = {"x":100, "y":0}

        self.rec = self.c.create_rectangle(5,5,40,40,fill = "white")
        self.c.pack()

        self.moveFrame = Frame(master, width=0, height = 0)
        self.moveFrame.bind("<Down>", self.moveDown)
        self.moveFrame.bind("<Up>", self.moveUp)
        self.moveFrame.bind("<Left>", self.moveLeft)
        self.moveFrame.bind("<Right>", self.moveRight)
        self.moveFrame.pack()
        self.moveFrame.focus_set()



        gridArray = {}
        """
        for x in range(0,20,1):
            for y in range(0, 20, 1):
                gridArray[(x, y)] = Label(self.master, height = 1, width = 1, text = "H")
                gridArray[(x, y)].grid(row = x, column = y)
        """
    def moveDown(self, event):
        self.c.move(self.rec, 0, 50)

    def moveUp(self, event):
        self.c.move(self.rec, 0, -50)

    def moveLeft(self, event):
        self.c.move(self.rec, -50, 0)

    def moveRight(self, event):
        self.c.move(self.rec, 50, 0)

    



def main():
    root = Tk()
    mainWindow(root)




    root.mainloop()


if __name__ == "__main__":
    main()