from datetime import date


class Tournament:
    """A class representing a tournament.

    Attributes
    ----------
    name:str
        the name of the tournament
    location: str
        the place where the tournament takes place
    rounds: list
        the list of tournament rounds
    players: list
        the list of tournament players
    description: str
        tournament description
    nb_turn: int
        the number of rounds of the tournament
    date:str
        the start date of the tournament
    end_date: str
        the end date of the tournament
    current_round: int
        the number of the current round of the tournament
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
        """_summary_
        Constructs all the necessary attributes for the Round object.

            Arguments:
                name -- the name of the tournament
                localisation -- the place where the tournament takes place
                rounds -- the list of tournament rounds
                players -- the list of tournament players
                description -- the description of the tournament

            Keyword Arguments:
                nb_turn -- the number of rounds of the tournament (default: {4})
                date -- the start date of the tournament (default: {date.today()})
                end_date -- the end date of the tournament (default: {""})
                current_round -- the number of the current round of the tournament (default: {1})
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
