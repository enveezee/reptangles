from tkinter import Canvas, Frame, Button, Label, LEFT, RIGHT, BOTH, X, Y, TOP, BOTTOM, CENTER
from board import Board
from player import Player


class Game(Frame):
    '''Reptangles Game class.'''
    def __init__(self, master, config):
        # Initialize Game Window
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.resizable(True, True)
        self.master.title('Reptangles')
        self.pack(expand=1, fill=BOTH)

        self.config = config

        # Player info display
        self.player_labels = []
        player_frame = Frame(self)
        player_frame.pack(side=TOP, fill=X)
        for i, p in enumerate(config.player):
            lbl = Label(player_frame, text=f"{p['name']}: 0", fg=p['color'], font=("Arial", 12, "bold"))
            lbl.pack(side=LEFT, expand=1)
            self.player_labels.append(lbl)

        # Main board canvas (large)
        self.board_canvas = Canvas(self, width=600, height=500, bg='white')
        self.board_canvas.pack(side=TOP, expand=1, fill=BOTH)

        # Controls frame (centered)
        controls_frame = Frame(self)
        controls_frame.pack(side=TOP, pady=8)
        self.tile_canvas = Canvas(controls_frame, width=64, height=64, bg='lightgray')
        self.tile_canvas.pack(side=LEFT, padx=8)
        self.tile_canvas.bind("<Button-1>", lambda e: self.swap())

        self.rotate_left_btn = Button(controls_frame, text="⟲", width=4, command=lambda: self.rotate('left'))
        self.rotate_left_btn.pack(side=LEFT, padx=2)
        self.place_btn = Button(controls_frame, text="Place", width=8, command=self.place)
        self.place_btn.pack(side=LEFT, padx=2)
        self.rotate_right_btn = Button(controls_frame, text="⟳", width=4, command=lambda: self.rotate('right'))
        self.rotate_right_btn.pack(side=LEFT, padx=2)

        # Board and turtles
        self.board = Board(config, self)
        self.board.createTurtles(self.board_canvas, self.tile_canvas)
        self.players = [Player(i+1, p['name'], p['color']) for i, p in enumerate(config.player)]
        self.active_player = 0

        self.init_game()


    def init_game(self):
        # Place start tile at center, position turtles, etc.
        self.board.place_start_tile()
        self.update_player_positions()


    def update_player_positions(self):
        # Position all player turtles on the start tile
        pass


    def place(self):
        # Place tile logic, scoring, end turn
        self.board.place_tile()
        self.score()
        self.end_turn()


    def rotate(self, direction):
        # Rotate active tile
        self.board.rotate_tile(direction)


    def swap(self):
        # Swap active/swap tile
        self.board.swap_tiles()


    def score(self):
        # Calculate and update score for active player
        pass


    def end_turn(self):
        # Switch active player, update UI, generate new tiles
        self.active_player = (self.active_player + 1) % len(self.players)
        # Update UI, etc.


    def player_collision(self):
        # Handle player collision/death
        pass

