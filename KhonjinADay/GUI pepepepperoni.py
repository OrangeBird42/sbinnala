from tkinter import *
import tkinter.messagebox
import random

readEpisode = open('episodeList.txt', "r")

def random_line(episodeList):
    lines = open(episodeList).read().splitlines()
    return random.choice(lines)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text= "Exit", command=self.clickExitButton)
        exitButton.place(x=0, y=0)

        episodeButton = Button(self, text="Click for Episode of the Day!", command=self.clickEpisodeButton)
        episodeButton.place(x=42, y=42)


    def clickExitButton(self):
        exit()
    
    def clickEpisodeButton(self):
        tkinter.messagebox.showinfo("Khonjin A Day!", random_line('episodeList.txt'))


readEpisode.close()
root = Tk()
app = Window(root)
root.wm_title("You may already be a winner.")
root.geometry("400x200")
root.mainloop()
