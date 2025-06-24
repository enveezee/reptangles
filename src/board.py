import turtle


class Board():
    '''A reptangles board object class.
    
     This class gets istantiated by the Game class, contains all the turtles,
    coordinates, and the methods for actual canvas drawing.
    '''
    def __init__(self, config, game):
        self.config = config
        self.game = game
        self.tiles = {}  # {(x, y): Tile}
        self.turtles = []
        self.board_turtle = None
        self.swap_turtle = None
        self.active_canvas = None
        self.viewport = (0, 0)  # Top-left of visible board


    def createTurtles(self, board_canvas, swap_canvas):
        '''Create turtles for reptangles.
        
         Turtle 0 is the board turtle that draws tiles, turtles 1-4 are the
        player's turtles, and turtle 5 is the swap tile turtle.
        '''
        # Player turtles
        for i in range(self.config.players):
            t = turtle.RawTurtle(board_canvas)
            t.hideturtle()
            t.speed('fastest')
            self.turtles.append(t)
        # Board turtle (for drawing tiles)
        self.board_turtle = turtle.RawTurtle(board_canvas)
        self.board_turtle.hideturtle()
        self.board_turtle.speed('fastest')
        self.active_canvas = board_canvas
        # Swap turtle (for drawing swap tile)
        self.swap_turtle = turtle.RawTurtle(swap_canvas)
        self.swap_turtle.hideturtle()
        self.swap_turtle.speed('fastest')


    def show_board_turtle(self):
        self.board_turtle.showturtle()

    def hide_board_turtle(self):
        self.board_turtle.hideturtle()

    def move_board_turtle_to_canvas(self, canvas):
        # Re-parent the board turtle to a different canvas
        # (tkinter turtle does not support moving turtles between canvases directly,
        # so you may need to destroy and recreate the turtle)
        pass

    def place_start_tile(self):
        # Place the initial tile at the center of the board
        pass

    def place_tile(self):
        # Place the selected tile on the board
        pass

    def rotate_tile(self, direction):
        # Rotate the active tile
        pass

    def swap_tiles(self):
        # Swap active and swap tile
        pass

    # Edge scrolling logic
    def scroll_board(self, dx, dy):
        # Adjust viewport and redraw visible tiles
        pass

