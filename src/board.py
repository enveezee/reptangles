import turtle


class Board():
    '''A reptangles board object class.
    
     This class gets istantiated by the Game class, contains all the turtles,
    coordinates, and the methods for actual canvas drawing.
    '''
    def __init__(self, config, player):
        self.board = config.board
        self.player = player
        self.tile = []      # List of all tiles on the board.
        self.turtle = []    # List of all turtles.


    def createTurtles(self, canvas):
        '''Create turtles for reptangles.
        
         Turtle 0 is the board turtle that draws tiles, turtles 1-4 are the
        player's turtles, and turtle 5 is the swap tile turtle.
        '''
        for i in range(5):
            # Append turtle to turtle list.
            self.turtle.append(turtle.RawTurtle(canvas))

            # Board turtles.
            if i == 0: 

                # Board and swap turtles are hidden and draw faster.
                self.turtle[i].hideturtle()
                self.turtle[i].speed('Fastest')

            # Player turtles.
            else:
                # Player turtles are the player's are user-defined.
                self.turtle[i].color()
                self.turtle[i].shape()
                self.turtle[i].speed()


    def drawCmd(self, turtle):
        '''Execute the draw command with the specified turtle.'''
        while self.drawcmd:
            cmd = self.drawcmd.pop(0)

            args = []
            if cmd in [A, C, F, G, L, R]:
                args.append(self.drawcmd.pop(0))

            if cmd in [C, G]:
                args.append(self.drawcmd.pop(0))

            turtleCmd = getattr(turtle, cmd)

            if args:
                turtleCmd(*args)
                continue

            turtleCmd()


    def drawPath(self, player):
        '''Draw path with the player's turtle.
         
         player is the player number to draw current tile path with.
        '''
        start = self.coord['player'][player] #! FML


        # Set the draw command for the tile the player is currently on.
        self.drawcmd = self.tile[tile].getPath(coord['player'][player][1])

        # Execute the draw command.
        self.drawCmd(self.turtle[player])


    def drawTile(self, tile=None, board=True):
        '''Draw tile on a canvas at coords.
        
         board is set to False to draw on swap tile canvas.

         tile is a Tile class object of the tile to draw, None to draw the
        start tile.
        '''
        if tile:

            # Set the draw command with a call to getPaths.
            self.drawcmd = tile.getPaths()

            # Check to see if we're drawing on the board or swap canvas.
            if board:
                self.drawCmd(self.turtle[0])    # Board canvas.

            else:
                self.drawCmd(self.turtle[5])    # Swap canvas.

        else:   # TODO: Draw start tile.
            pass

    def moveTurtles(self):
        '''Move the turtles along the paths.'''
        pass

