import random

# ! Headings (30,45,90 deg increments):
E = 0
ENE = 30
NE = 45
NNE = 60
N = 90
NNW = 120
NW = 135
WNW = 150
W = 180
WSW = 210
SW = 225
SSW = 240
S = 270
SSE = 300
SE = 315

# ! Turtle Commands:
ANGLE = 'setheading'
CIRCLE = 'circle'
DOWN = 'pendown'
FORWARD = 'forward'
GOTO = 'goto'
LEFT = 'left'
RIGHT = 'right'
UP = 'penup'

# ! Tile Data:
TILE = {
    'hexagon': {                # ! Not implemented yet.
        'angle': 30,            # ? Angle of each corner.
        'sides': 6,             # ? Number of sides.
    },
    'square': {                 # ! Square Tile Data
        'angle': 90,            # ? Angle of each corner.
        'delta': [              # ? Distance between start and end point.
            None,
            [(3, 180)],         # * Delta 1 (Turn around path).
            [(7, 90), 6],       # * Delta 2 (Backward J arc path).
            [(13, 90)],         # * Delta 3 (C arc path).
            [                   # * Delta 4 (Diagonal path).
                [
                    (6, -20),   # 1 to 5.
                    (-6, -20),  # 2 to 6.
                    (-20, -6),  # 3 to 7.
                    (-20, 6),   # 4 to 8.
                    (-6, 20),   # 5 to 1.
                    (6, 20),    # 6 to 2.
                    (20, 6),    # 7 to 3.
                    (20, -6),   # 8 to 4.
                ]
            ],
            [20],               # * Delta 5 (Straigh path).
            [6, (-7, 90)],      # * Delta 6 (J arc path).
            [(-7, 90)],         # * Delta 7 (Corner arc path).
        ],
        'home': {               # ? Homing points and headings.
            X = [0, 7, 13, 20, 20, 13, 7, 0, 0] # X offset.
            Y = [0, 0, 0, 7, 13, 20, 20, 13, 7] # Y offset.
            Z = [E, S, S, W, W, N, N, E, E]     # Heading.
        },
        'length': 20,           # ? Length of each side.
        'sides': 4,             # ? Number of sides.
    },
    'triangle': {               # ! Not implemented yet.
        'angle': 120,           # ? Angle of each corner.
        'sides': 3,             # ? Number of sides.
    },
}

# TODO: Will be a config option for scale factor.
scale = 3


class Tile():
    '''A reptangles tile object class.
    
     This class is instantiated twice per turn for the player's active and
    swap tile, the tile placed is put into the Board.tile list and the other is
    discarded.

     This class must be instantiated with the board offsets (x, y) of the top
    left corner in canvas coordinates.

     This class will randomly generate a map of endpoint connections and has
    methods for drawing the tile, and getting draw commands for a single path
    or all 4 paths on the tile. It also contains a method to rotate the mapping
    of endpoints to redraw a rotated tile.

     This class DOES NOT have access to the turtles, nor does it actually draw
    ANYTHING, it merely returns a list of turtle commands to be used by the
    Board class to do the actual drawing.
    '''
    def __init__(self, offset):
        # Generate endpoint map for this tile.
        self.endpoint = self.randomize()

        # Number of paths traversed on this tile by a player.
        self.paths = 0

        # Which endpoints have players on them
        #self.players = [0,0,0,0,0,0,0,0]

        # Set board coordinate offsets
        self.x, self.y = offset


    def draw(self):
        '''Return the draw command for the tile.
        
         This method is used to initially draw the tile, it returns a command
        of all instructions to draw the entire tile including the boarder and
        background.
        '''
        # Initalize the draw command to the top left corner of the tile.
        drawcmd = self.home()
        # Border.
        drawcmd.extend(BORDER)
        # 4 paths on the tile.
        drawcmd.extend(self.getPaths)
        # Return the drawcmd.
        return drawcmd


    def getPath(self, start):
        '''Return the draw command for given endpoints on the tile.
        
         start is an the endpoint for turtle's current location.
        
         This method is used for when you only need to draw one path, as in 
        when the player is traversing a tile on a single path. It is also
        called by getPaths to get all 4 paths for the tile.

         This method DOES NOT put the pen up or home and adjust heading.
        It assumes you are already oriented at the start point with the proper
        heading already applied and the pen down.
        '''
        # Extract the end point from the tile.
        end = self.endpoint[start]
        
        # Calculate the delta of how many points away the endpoint is clockwise.
        delta = abs(start - end)

        # Static draw data for the delta and data[0] True if going in reverse.
        data = [
            start>end,      # Negative delta True/False
            [(V, H)],       # Delta 1
            [(O, Q), M],    # Delta 2
            [(J, Q)],       # Delta 3
            [None],         # Delta 4
            [T],            # Delta 5
            [M, (-O, Q)],   # Delta 6
            [(-O, Q)],      # Delta 7
        ]

        # List to contain draw commands for the path between endpoints.
        drawcmd = []

        # Iterate over data for the given delta.
        for i in data[delta]:

            # Draw an arc.
            if type(i) == 'tuple':

                # Extract radius and angle of the arc from the tuple.
                radius, angle = i

                # If drawing in reverse, multiply radius by -1.
                if data[0]:
                    radius = radius * -1

                # Append the draw command for the arc to the list.
                drawcmd.extend([C, radius * scale, angle])

            # Draw a line.
            elif type(i) == 'int':

                if data[0]:
                
                    # If drawing in reverse, multiply i by -1.
                    i = i * -1                

                # Append the draw command for the line to the list.
                drawcmd.extend([F, i * scale])

            # Draw diagonal line.
            elif i[0] == None:
        
                # Set x,y offsets for the end point.
                X, Y = [
                    (M, -T),    # 1 to 5
                    (-M, -T),   # 2 to 6
                    (-T, -M),   # 3 to 7
                    (-T, M),    # 4 to 8
                    (-M, T),    # 5 to 1
                    (M, T),     # 6 to 2
                    (T, M),     # 7 to 3
                    (T, -M)     # 8 to 4
                ][start]
        
                # Append draw command for the line to the list.
                drawcmd.extend([G, X + self.x, Y + self.y])
                return drawcmd

        # Return the draw commands.
        return drawcmd


    def getPaths(self):
        '''Return a draw command for all paths on this tile.
        
         This method is for when drawing the paths initially and on rotate or
        on swap, when you need to draw them all at once.

         This method DOES lift the pen, home, and orient headings. It creates
        a ready to execute draw command to draw all paths for the tile. However
        it DOES NOT draw the tile boarder or background.
        '''
        # Set scale.
        J, M, O, T, V = self.scale()

        # List of endpoints not yet drawn.
        endpoints = [1, 2, 3, 4, 5, 6, 7, 8]

        # Home turtle on tile.
        drawcmd = self.home()

        # Loop 4 times for the 4 paths to draw.
        for i in range(4):

            # Pop start point from list
            start = endpoints.pop(0)

            # Get index of end point.
            idx = self.endpoint[start]

            # Pop end point from list.
            end = endpoints.pop(idx)

            # Add instructions to move to start point to drawcmd.
            drawcmd.extend(self.home(start))

            # Add path to drawcmd.
            drawcmd.extend(self.getPath(start))


    def home(self, point=0):
        '''Return draw command to home turtle on tile.
        
         This method homes the turtle to a given endpoint of the tile with the
        proper heading, pen down, ready to draw a path from that point. If no
        endpoint is specified, it homes to the top left of the tile with the
        pen up, facing east.
        '''
        # Set scale.
        J, M, O, T, V = self.scale()

        # Set x,y offsets for point.
        X = [0, O, J, T, T, J, O, 0, 0][point] + self.x
        Y = [0, 0, 0, O, J, T, T, J, O][point] + self.y

        # Set heading for point.
        Z = [E, S, S, W, W, N, N, E, E][point]

        # Set draw command.
        drawcmd = [U, G, X, Y, A, Z]

        # Put pen down if point is specified.
        if point:
            drawcmd.append(D)

        # Return draw command.
        return drawcmd


    def randomize(self):
        '''Generate randomized endpoint mappings for this tile.'''
        # Randomized endpoint map.
        endpoint = {}

        # All endpoints lists.
        endpoints = [1, 2, 3, 4, 5, 6, 7, 8]

        # Iterate over all endpoints
        while endpoints:

            # Pop the start point off the list of remaining endpoints.
            start = endpoints.pop(0)

            # Choose a random endpoint from the list remaining.
            end = random.choice(endpoints)

            # Set index of the end point in the list.
            idx = endpoints.index(end)

            # Pop the end point off the list and map it to the start point.
            endpoint[start] = endpoints.pop(idx)

            # Map the start point to the end point.
            endpoint[end] = start

        # Set new endpoint map on Tile object.
        self.endpoint = endpoint


    def rotate(self, direction):
        '''Rotate the tile in a direction.
        
         direction is 0 for left or counterclockwise, 1 for right or clockwise.
        '''
        # Rotated endpoint map.
        endpoint = {}

        # Current endpoint map.
        endpoints = self.endpoint

        # Rotation map for a given direction (0=Left/CCW, 1=Right/CW)
        rotmap = [[3, 4, 5, 6, 7, 8, 1, 2], [7, 8, 1, 2, 3, 4, 5, 6]][direction]

        for point in endpoints:

            start = rotmap.index(point)
            end = rotmap.index(endpoints[point])
            endpoint[start], endpoint[end] = [end, start]

        self.endpoint = endpoints


    def scale(self, scale):
        '''Scale Tile measurements.'''
        return [J * scale, M * scale, O * scale, T * scale, V * scale]

