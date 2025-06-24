#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, colorchooser, simpledialog
from config import Config
from game import Game

class Reptangles(tk.Frame):
    '''Reptangles GUI class.'''
    def __init__(self, master):
        # Initialize mainwindow
        super().__init__(master)
        self.master = master
        self.master.geometry("600x500")
        self.master.title('Reptangles')
        self.pack(expand=1, fill=tk.BOTH)
        self.config = Config()
        self.createSetupForm()


    def callback(self, event):
        widget = f'{event.widget}'.split('.')[-1]


    def newGame(self):
        config = Config()
        config.players = 4
        game = Game(tk.Toplevel(), config)
        game.mainloop()


    def createSetupForm(self):
        # Clear any existing widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Number of players
        tk.Label(self, text="Number of Players:").pack()
        self.num_players = tk.IntVar(value=4)
        tk.Spinbox(self, from_=1, to=4, textvariable=self.num_players, command=self.updatePlayerFields).pack()

        # Player fields
        self.player_frames = []
        self.player_vars = []
        self.updatePlayerFields()

        # Tile sides
        tk.Label(self, text="Tile Sides:").pack()
        self.tile_sides = tk.IntVar(value=4)
        ttk.Combobox(self, values=[3, 4, 6], textvariable=self.tile_sides, state="readonly").pack()

        # Board size
        tk.Label(self, text="Board Size:").pack()
        self.board_size = tk.StringVar(value="9x9")
        ttk.Combobox(self, values=["7x7", "9x9", "11x11", "15x15", "Infinite"], textvariable=self.board_size, state="readonly").pack()

        # Start Game button
        tk.Button(self, text="Start Game", command=self.startGame).pack(pady=10)

        # Game Options button
        tk.Button(self, text="Game Options", command=self.openOptions).pack()

    def updatePlayerFields(self):
        # Remove old player frames
        for frame in self.player_frames:
            frame.destroy()
        self.player_frames.clear()
        self.player_vars.clear()
        # Add new player fields
        for i in range(self.num_players.get()):
            frame = tk.Frame(self)
            frame.pack()
            name_var = tk.StringVar(value=f"Player {i+1}")
            color_var = tk.StringVar(value=["blue", "red", "green", "yellow"][i % 4])
            tk.Label(frame, text=f"Player {i+1} Name:").pack(side=tk.LEFT)
            tk.Entry(frame, textvariable=name_var).pack(side=tk.LEFT)
            tk.Label(frame, text="Color:").pack(side=tk.LEFT)
            tk.Entry(frame, textvariable=color_var, width=8).pack(side=tk.LEFT)
            # TODO: Add turtle icon selection
            self.player_vars.append((name_var, color_var))
            self.player_frames.append(frame)

    def startGame(self):
        # Gather config
        self.config.players = self.num_players.get()
        self.config.player = []
        for name_var, color_var in self.player_vars:
            self.config.player.append({
                "name": name_var.get(),
                "color": color_var.get(),
                # "icon": ... # TODO: Add icon selection
            })
        self.config.tile_sides = self.tile_sides.get()
        self.config.board_size = self.board_size.get()
        # Hide setup, launch game
        self.pack_forget()
        game = Game(tk.Toplevel(), self.config)
        game.mainloop()

    def openOptions(self):
        # Open options dialog
        OptionsDialog(self.master, self.config)

class OptionsDialog(simpledialog.Dialog):
    def __init__(self, parent, config):
        self.config = config
        super().__init__(parent, title="Game Options")

    def body(self, master):
        tk.Label(master, text="Scroll Speed:").grid(row=0, column=0)
        self.scroll_speed = tk.IntVar(value=getattr(self.config, "scroll_speed", 10))
        tk.Entry(master, textvariable=self.scroll_speed).grid(row=0, column=1)
        tk.Label(master, text="Fullscreen:").grid(row=1, column=0)
        self.fullscreen = tk.BooleanVar(value=getattr(self.config, "fullscreen", False))
        tk.Checkbutton(master, variable=self.fullscreen).grid(row=1, column=1)
        return master

    def apply(self):
        self.config.scroll_speed = self.scroll_speed.get()
        self.config.fullscreen = self.fullscreen.get()
        self.config.save()

if __name__ == '__main__':
    reptangles = Reptangles(tk.Tk())
    reptangles.mainloop()

