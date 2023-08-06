DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

TURNS = {
    'L': {
        'N': 'W',
        'E': 'N',
        'S': 'E',
        'W': 'S'
    },
    'R': {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
}