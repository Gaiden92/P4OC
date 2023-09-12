from datetime import date


class Tournament:
    """Une classe représentant un tournoi.

    Attributs
    ----------
    name : str
        le nom du tournoi
    localisation : str
        l'endroit où à lieu le tournoi
    rounds : list
        la liste des tours du tournoi
    players : list
        la liste des joueurs du tournoi
    description : str
        la description du tournoi
    nb_turn : int
        le nombre de tour du tournoi
    date : str
        la date de début du tournoi
    end_date : str
        la date de fin du tournoi
    current_round : int
        le numéro du tour actuel du tournoi

    """

    def __init__(
        self,
        name: str,
        localisation: str,
        rounds: list,
        players: list,
        description: str,
        nb_turn=4,
        date: str = date.today(),
        end_date: str = "",
        current_round: int = 1,
    ) -> None:
        """Construit tous les attributs nécessaire pour l'objet Round.

        Arguments:
            name -- le nom du tournoi
            localisation -- l'endroit où à lieu le tournoi
            rounds -- la liste des tours du tournoi
            players -- la liste des joueurs du tournoi
            description -- la description du tournoi

        Keywords Arguments:
            nb_turn -- le nombre de tour du tournoi (default: {4})
            date -- la date de début du tournoi (default: {date.today()})
            end_date -- la date de fin du tournoi (default: {""})
            current_round -- le numéro du tour actuel du tournoi (default: {1})
        """
        self.name = name
        self.date = str(date)
        self.localisation = localisation
        if nb_turn == "":
            self.nb_turn = 4
        else:
            self.nb_turn = int(nb_turn)
        self.rounds = rounds
        self.players = players
        self.description = description
        self.end_date = end_date
        if len(self.rounds) >= current_round - 1:
            self.current_round = len(self.rounds)
        else:
            self.current_round = current_round
