from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from main import Snake

class OptionsScreen:
    def __init__(self, master):
        self.master = master


class MenuScreen:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,500)
        self.master.maxsize(400,500)
        self.master.configure(bg = "black")
        #self.master.configure(bg = "black")

        start_Button = ttk.Button(self.master, text = "Start Snake", command = self.startGame)
        options_Button = ttk.Button(self.master, text = "Options", command = self.options)
        start_Button.grid(column = 3, row = 1, pady = 25)
        options_Button.grid(column = 3, row = 3, pady = 25)
        

        img = ImageTk.PhotoImage(Image.open("SnakeLogo.gif"))
        #self.canvas = Canvas(self.master, width = img.width(), height = img.height())
        self.snakeImage = Label(self.master, image = img, background = "black")
        self.snakeImage.image = img
        self.snakeImage.grid(column = 1, row = 0, columnspan = 5, padx = 100)
        

    def startGame(self):
        snakeGame = Tk()
        Snake(snakeGame)
        snakeGame.mainloop()
    def options(self):
        self.length = 7
        options = Tk()
        length_Label = Label(options, text = "Length of Snake")
        lengthNumber_Label = Label(options, text = str(self.length))
        length_Button1 = Button(options, text = "<-")
        length_Button2 = Button(options, text = "->")

        length_Label.grid(row = 0, column = 0)
        lengthNumber_Label.grid(row = 0, column = 0, rowspan = 2)
        length_Button1.grid(row = 1, column = 1)
        length_Button2.grid(row = 1, column = 2)
        options.mainloop()
        
        
        
        

def main():
    root = Tk()
    MenuScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
