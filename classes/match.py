class Match:
    """Une classe qui représente un match.

    Attributes
    ----------
    joueur1 : list
        le nom et le score du joueur1
    joueur2 : list
        le nom et le score du joueur2

    Methods
    -------
    match_serialized(self):
        Convertie un objet Match en une liste.
    """

    def __init__(self, player1, player2) -> None:
        """Constructs tous les attributs nécessaire pour l'objet Match.

        Parameters
        ----------
            joueur1 : list
                le nom et le score du joueur1
            joueur2 : list
                le nom et le score du joueur2
        """
        self.player1 = player1
        self.player2 = player2

    def match_serialized(self):
        """
        Convertie un objet Match en une liste.

        Parameters
        ----------
        None

        Returns
        -------
        list
        """
        list_match = (self.player1, self.player2)

        return list_match
