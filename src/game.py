from tkinter import Canvas, Frame
from board import Board
from player import Player
from tile import Tile


class Game(Frame):
    '''Reptangles Game class.'''
    def __init__(self, master, config):
        # Initialize Game Window
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.master.resizable(True, True)
        self.master.title('Reptangles')
        self.pack()

        self.canvas = Canvas()
        self.canvas.pack(expand=1, fill='both')

        self.player = Player(config.players)

        self.board = Board(config, self.player)


    def place(self):
        pass


    def rotate(self, direction):
        pass


    def swap(self):
        pass

