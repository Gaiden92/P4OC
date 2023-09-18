class Match:
    """A class that represents a match.

        Attributes
        ----------
        player1: list
            player name and score1
        player2: list
            player name and score2

        Methods
        -------
        match_serialized(self):
            Convert a Match object to a list.
    """

    def __init__(self, player1: list, player2: list) -> None:
        """Construit tous les attributs nécessaire pour l'objet Match.
        Arguments:
            player1 -- le nom et le score du joueur1
            player2 -- le nom et le score du joueur2
        """

        self.player1 = player1
        self.player2 = player2

        self.player1_id = player1[0]
        self.player1_score = player1[1]

        self.player2_id = player2[0]
        self.player2_score = player2[1]

    def serialize_match(self) -> list:
        """
        Converts a Match object to a list.

        Settings
        ----------
        None

        Return
        -------
        list
        """
        list_match = (self.player1, self.player2)

        return list_match
