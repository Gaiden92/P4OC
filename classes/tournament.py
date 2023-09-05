from datetime import date, datetime

class Tournament:

    def __init__(self, name:str, localisation:str, rounds:list, players:list, description: str, nb_turn=4, date=date.today(), end_date="") -> None:
        self.name           = name
        self.date           = str(date)
        self.localisation   = localisation
        self.nb_turn        = nb_turn
        self.rounds         = rounds
        self.players        = players
        self.description    = description
        self.end_date       = end_date