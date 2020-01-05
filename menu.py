from tkinter import *
from PIL import ImageTk, Image

class MenuScreen:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,500)
        self.master.maxsize(400,500)
        self.master.configure(bg = "black")
        #self.master.configure(bg = "black")

        start_Button = Button(self.master, text = "Start Snake", bg = "white", command = self.startGame)
        options_Button = Button(self.master, text = "Options", command = self.options)
        start_Button.pack(side = "left")
        options_Button.pack(side = "right")
        

        img = ImageTk.PhotoImage(Image.open("SnakeLogo.gif"))
        #self.canvas = Canvas(self.master, width = img.width(), height = img.height())
        self.snakeImage = Label(self.master, image = img, bg = "black")
        self.snakeImage.image = img
        self.snakeImage.pack(anchor = "center")
        

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
