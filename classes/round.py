from datetime import date
from datetime import datetime
from random import shuffle

from .match import Match


class Round:
    def __init__(self, name=0) -> None:
        self.name = name
        self.start_date = str(date.today())
        self.start_hour = str(datetime.now().time().strftime("%H:%M:%S"))
        self.end_date = ""
        self.end_hour = ""

        self.matchs = []

    def serialize_round(self):
        dict_round = {
            "name": self.name,
            "start_date": self.start_date,
            "start_hour": self.start_hour,
            "end_date": self.end_date,
            "end_hour": self.end_hour,
            "matchs": self.matchs,
        }

        return dict_round

    def generate_first_round(self, list_players):
        shuffle(list_players)
        length_sorted_list = len(list_players)

        index = 0
        while index < length_sorted_list:
            score1 = 0
            score2 = 0
            match = Match(
                [list_players[index].firstname, score1],
                [list_players[index + 1].firstname, score2],
            ).match_serialized()
            self.matchs.append(match)
            index += 2

        return self.matchs
