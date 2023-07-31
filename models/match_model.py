import tinydb, datetime, random

class Match:
    def __init__(self, player1, player2) -> None:
        self.date = datetime.now()
        self.players    = [player1, player2]
        
        self.score_match = self.score(player1, player2)

