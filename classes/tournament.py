from datetime import date


class Tournament:
    def __init__(
        self,
        name: str,
        localisation: str,
        rounds: list,
        players: list,
        description: str,
        nb_turn=4,
        date=date.today(),
        end_date="",
        current_round=1,
    ) -> None:
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
        if len(self.rounds) >= current_round-1:
            self.current_round = len(self.rounds)
        else:
            self.current_round = current_round
