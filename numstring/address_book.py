import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    (?P<last_name>[-\w\s?]*),\s   # Last Names
    (?P<first_name>[-\w\s?]+):\s   # First Names
    (?P<score>[\d]+)   # Score
''', string, re.X | re.M)


class Player:
    last_name = ""
    first_name = ""
    score = ""

    def __init__(self, last_name=last_name, first_name=first_name, score=score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score