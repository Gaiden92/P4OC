class Match:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2

        self.result = None
    
    def match_serialized(self):
        list_match =    (
                            self.player1,
                            self.player2
                        )

        return list_match