from tkinter import *

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake")
        self.BeginGame_Button = Button(self.master, text = "Begin Game")
        self.BeginGame_Button.pack()

        


def main():
    root = Tk()
    Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()