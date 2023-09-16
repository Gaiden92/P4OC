class Match:
    """Une classe qui représente un match.

    Attributs
    ----------
    joueur1 : list
        le nom et le score du joueur1
    joueur2 : list
        le nom et le score du joueur2

    Methodes
    -------
    match_serialized(self):
        Convertie un objet Match en une liste.
    """

    def __init__(self, player1: list, player2: list) -> None:
        """Construit tous les attributs nécessaire pour l'objet Match.

        Paramètres
        ----------
            joueur1 : list
                le nom et le score du joueur1
            joueur2 : list
                le nom et le score du joueur2
        """
        self.player1 = player1
        self.player2 = player2

        self.player1_id = player1[0]
        self.player1_score = player1[1]

        self.player2_id = player2[0]
        self.player2_score = player2[1]

    def serialize_match(self) -> list:
        """
        Convertie un objet Match en une liste.

        Paramètres
        ----------
        None

        Retourne
        -------
        list
        """
        list_match = (self.player1, self.player2)

        return list_match
