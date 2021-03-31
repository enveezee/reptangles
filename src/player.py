

class Player():
    '''Reptangles player class.'''
    def __init__(self, players):
        for i in range(1, players + 1):
            setattr(self, f'{i}', {
                    'color': [None, 'blue','red','green','yellow'][i],
                    'name' : f'Player {i}',
                    'moves': True,
                    'score': 0,
                }
            )

