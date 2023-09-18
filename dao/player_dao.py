from tinydb import TinyDB
from tinydb import Query

from models.player import Player


class PlayerDao:
    """A class representing the player table for the <Player> class.
    """

    def __init__(self, database: str) -> None:
        """Constructs all the attributes necessary for the class.

        Arguments:
            database -- The database with which the class will communicate.
        """
        self.db = TinyDB(database, indent=4, separators=(",", ": "))
        self.player_table = self.db.table("players")
        self.player_query = Query()

    def create_player(self, player: object) -> None:
        """The method allows you to add a player to the database.

        Arguments:
            player -- a <player> object
        """
        player_serialize = player.serialize_player()
        self.player_table.insert(player_serialize)

    def get_all_players(self) -> list:
        """Retrieves the list of all players in the database.

        Returns:
             All players in the database as a list of <player> objects
        """
        all_players_list = []
        for player in self.player_table.all():
            all_players_list.append(
                Player(
                    player["id"],
                    player["lastname"],
                    player["firstname"],
                    player["gender"],
                    player["birthdate"],
                )
            )
        return all_players_list

    def get_player(self, lastname: str, firstname: str) -> None | object:
        """Retrieves a player whose first and last name were indicated in the parameters.

        Arguments:
            lastname -- the player's name
            firstname -- the player's first name

        Returns:
            If the player is present in the database:
                a <player> object containing player information
            else None
        """
        player = self.player_table.get(
            self.player_query.lastname == lastname
            and self.player_query.firstname == firstname
        )
        if player:
            return Player(
                player["id"],
                player["lastname"],
                player["firstname"],
                player["gender"],
                player["birthdate"],
            )
        else:
            return None

    def update_player(
        self, updates: list, column: str, lastname: str, firstname: str
    ) -> bool:
        """Update a player's data by searching by firstname and lastname.

        Arguments:
            updates -- the new data
            column -- the column to update (lastame, firstname, age,...)
            lastname -- the player's lastname
            firstname -- the player's firstname

        Returns:
            bool: If the update was performed, the function returns True
                   else the function returns False
        """
        if self.player_table.update(
            {column: updates},
            (self.player_query.lastname == lastname)
            and (self.player_query.firstname == firstname),
        ):
            return True
        else:
            return False

    def delete_player(self, lastname: str, firstname: str) -> bool:
        """Remove a player by searching by firstname and lastname.

        Arguments:
            lastname -- the player's lastname
            firstname -- the player's firstname

        Returns:
            bool: If deletion was performed, the function returns True
                  else the function returns False
        """
        if self.player_table.remove(
            (self.player_query.lastname == lastname)
            and (self.player_query.firstname == firstname)
        ):
            return True
        else:
            return False

    def get_player_by_id(self, id: str) -> object:
        """Retrieve a player object by his id

        Arguments:
            id -- a player's id

        Returns:
            a <player> object
        """
        player = self.player_table.get(self.player_query.id == id)
        if player:
            return Player(
                player["id"],
                player["lastname"],
                player["firstname"],
                player["gender"],
                player["birthdate"],
            )
        else:
            return None
