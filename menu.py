from tkinter import *

class MenuScreen:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,500)
        self.master.maxsize(400,500)
        #self.master.configure(bg = "black")

        start_Button = Button(self.master, text = "Start Snake", command = self.startGame)
        options_Button = Button(self.master, text = "Options", command = self.options)
        start_Button.pack()
        options_Button.pack()

        img = PhotoImage(file = "SnakeLogo.gif")
        #self.canvas = Canvas(self.master, width = img.width(), height = img.height())
        snakeImage = Label(self.master, image = img)
        snakeImage.pack(side = LEFT)

    def startGame(self):
        pass
    def options(self):
        pass
        

def main():
    root = Tk()
    MenuScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()



