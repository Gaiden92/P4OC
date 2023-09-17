from datetime import date
from datetime import datetime
from random import shuffle

from .match import Match


class Round:
    """A class representing a round.

    Attributes
    ----------
    name:str
        the name of the tour
    start_date: str
        the start date of the tour
    start_hour: str
        start time of the tour
    end_date: str
        the end date of the tour
    end_hour: str
        end time of the tour

    Methods
    -------
    serialize_round(self):
        Converts a Round object to a dictionary.
    generate_first_round(self, list_players):
        Generates the 1st round from the list of players registered for the tournament
    """

    def __init__(self, name: int = 0) -> None:
        """Constructs all the necessary attributes for the Round object.

        Keyword Arguments:
            name -- The name of the tour (default: {0})
        """
        self.name = name
        self.start_date = str(date.today())
        self.start_hour = str(datetime.now().time().strftime("%H:%M:%S"))
        self.end_date = ""
        self.end_hour = ""

        self.matchs = []

    def serialize_round(self) -> dict:
        """Converts a Round object to a dictionary.

        Returns:
            A dictionary containing tour information.
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
        """Generates the 1st round from the list of players registered for the tournament

        Arguments:
            list_players -- list of players

        Returns:
            _description_ list of <Match> objects
        """
        shuffle(list_players)
        length_sorted_list = len(list_players)

        index = 0
        while index < length_sorted_list:
            score1 = 0
            score2 = 0
            match = Match(
                [list_players[index].id, score1],
                [list_players[index + 1].id, score2],
            ).serialize_match()
            self.matchs.append(match)
            index += 2

        return self.matchs
