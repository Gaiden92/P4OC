from tinydb import TinyDB
from tinydb import Query

from models.tournament import Tournament


class TournamentDao:
    """A class representing the tournament table for the <Tournament> class.
    """
    def __init__(self, database: str) -> None:
        """Constructs all the attributes necessary for the class.

        Arguments:
            database -- The database with which the class will communicate.
        """
        self.db = TinyDB(database, indent=4, separators=(",", ": "))
        self.tournament_query = Query()
        self.tournament_table = self.db.table("tournois")

    def create_tournament(self, tournament: object) -> None:
        """Function allowing you to create a tournament in the database.

        Arguments:
            tournament -- a Tournament object

        Returns:
            bool
        """
        if self.tournament_table.insert(
            {
                "name": tournament.name,
                "localisation": tournament.localisation,
                "nb_turn": tournament.nb_turn,
                "players": tournament.players,
                "rounds": tournament.rounds,
                "description": tournament.description,
                "date": tournament.date,
                "end_date": tournament.end_date,
                "current_round": tournament.current_round,
            }
        ):
            return True
        else:
            return False

    def get_tournaments(self) -> object:
        """Function allowing you to retrieve all tournaments in the database.

        Returns:
            object : <Tournament>
        """
        tournaments = self.tournament_table.all()

        return [
            Tournament(
                tournament["name"],
                tournament["localisation"],
                tournament["rounds"],
                tournament["players"],
                tournament["description"],
                tournament["nb_turn"],
                tournament["date"],
                tournament["end_date"],
                tournament["current_round"],
            )
            for tournament in tournaments
        ]

    def get_tournament_by_name(self, name: str) -> object | None:
        """Function allowing you to retrieve a tournament from the database via its name.

        Arguments:
            name -- str : name of a tournament

        Returns:
            object : <Tournament>
        """
        tournament = self.tournament_table.get(self.tournament_query.name == name)
        if tournament:
            return Tournament(
                tournament["name"],
                tournament["localisation"],
                tournament["rounds"],
                tournament["players"],
                tournament["description"],
                tournament["nb_turn"],
                tournament["date"],
                tournament["end_date"],
                tournament["current_round"],
            )
        else:
            return None

    def update_tournament(self, updates: str, name: str) -> None:
        """Edit a tournament via his name.

        Arguments:
            updates -- str : the updates
            name -- str : the name of the tournament
        """
        self.tournament_table.update(
            {"name": updates}, self.tournament_query.name == name
        )

    def update_round_tournament(self, updates: list, name: str) -> None:

        """Modify the round of a tournament via his name.

        Arguments:
            updates -- list : the rounds list
            name -- str : the tournament's name
        Returns:
            None
        """
        tournament = updates

        self.tournament_table.update(
            {
                "name": tournament.name,
                "localisation": tournament.localisation,
                "players": tournament.players,
                "rounds": tournament.rounds,
                "description": tournament.description,
                "date": tournament.date,
                "end_date": tournament.end_date,
                "current_round": tournament.current_round,
            },
            self.tournament_query.name == name,
        )

    def delete_tournament(self, name: str) -> bool | None:
        """Delete a tournament by his name.

        Arguments:
            name -- str : tournament's name

        Returns:
            bool
        """
        if self.tournament_table.remove(self.tournament_query.name == name):
            return True
        else:
            return False

    def none_tournament_register(self) -> bool:
        """Verify if unless one tournament is register.

        Returns:
            bool
        """
        if len(self.tournament_table) == 0:
            return True
        else:
            return False

    def update_players_tournament(self, list: list, name: str) -> None:
        """Update the players list of a tournament by his name.

        Arguments:
            list -- list : a list of players
            name -- str : the tournament's name
        """
        self.tournament_table.update(
            {"players": list}, self.tournament_query.name == name
        )
