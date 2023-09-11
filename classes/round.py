from datetime import date
from datetime import datetime
from random import shuffle

from .match import Match


class Round:
    """Une classe représentant un tour.

    Attributs
    ----------
    name : str
        le nom du tour
    start_date : str
        la date de début du tour
    start_hour : str
        l'heuere de début du tour
    end_date : str
        la date de fin du tour
    end_hour : str
        l'heure de fin du tour

    Methodes
    -------
    serialize_round(self):
        Convertie un objet Round en un dictionnaire.
    generate_first_round(self, list_players):
        Génére le 1er tour à partir de la liste des joueurs inscrits au tournoi
    """

    def __init__(self, name: int = 0) -> None:
        """Construit tous les attributs nécessaire pour l'objet Round.

        Paramètres:
            name -- Le nom du tour (default: {0})
        """
        self.name = name
        self.start_date = str(date.today())
        self.start_hour = str(datetime.now().time().strftime("%H:%M:%S"))
        self.end_date = ""
        self.end_hour = ""

        self.matchs = []

    def serialize_round(self) -> dict:
        """Convertie un objet Round en un dictionnaire.

        Retourne:
            Un dictionnaire contenant les informations du tour.
        """
        dict_round = {
            "name": self.name,
            "start_date": self.start_date,
            "start_hour": self.start_hour,
            "end_date": self.end_date,
            "end_hour": self.end_hour,
            "matchs": self.matchs,
        }

        return dict_round

    def generate_first_round(self, list_players: list) -> list:
        """Génére le 1er tour à partir de la liste des joueurs inscrits au tournoi

        Arguments:
            list_players -- une liste de joueurs

        Retourne:
            une liste d'objet <Match>
        """
        shuffle(list_players)
        length_sorted_list = len(list_players)

        index = 0
        while index < length_sorted_list:
            score1 = 0
            score2 = 0
            match = Match(
                [list_players[index].firstname, score1],
                [list_players[index + 1].firstname, score2],
            ).serialize_match()
            self.matchs.append(match)
            index += 2

        return self.matchs
