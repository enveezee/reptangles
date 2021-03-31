#!/usr/bin/env python3
import tkinter as tk
from config import Config
from game import Game

class Reptangles(tk.Frame):
    '''Reptangles GUI class.'''
    def __init__(self, master):
        # Initialize mainwindow
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.master.resizable(True, True)
        self.master.title('Reptangles')
        self.pack()


        # Create menubar.
        self.createMenu()


    def callback(self, event):
        widget = f'{event.widget}'.split('.')[-1]


    def createMenu(self):
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label="New", command=self.newGame)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.menubar)


    def newGame(self):
        config = Config()
        config.players = 4
        game = Game(tk.Toplevel(), config)
        game.mainloop()


if __name__ == '__main__':
    reptangles = Reptangles(tk.Tk())
    reptangles.mainloop()

