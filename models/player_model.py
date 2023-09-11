from tinydb import TinyDB
from tinydb import Query

from classes.player import Player


class PlayerModel:
    def __init__(self, database) -> None:
        self.db = TinyDB(database, indent=4, separators=(",", ": "))
        self.player_table = self.db.table("players")
        self.player_query = Query()

    def create_player(self, player):
        player_serialize = player.serialize_player()
        self.player_table.insert(player_serialize)

    def get_all_players(self):
        all_players_list = []
        for player in self.player_table.all():
            all_players_list.append(
                Player(
                    player["id"],
                    player["lastname"],
                    player["firstname"],
                    player["gender"],
                    player["birthdate"],
                    player["rank"],
                )
            )
        return all_players_list

    def get_player(self, lastname, firstname):
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
                player["rank"],
            )
        else:
            return None

    def update_player(self, updates, column, lastname, firstname):
        if self.player_table.update(
            {column: updates},
            (self.player_query.lastname == lastname)
            and (self.player_query.firstname == firstname),
        ):
            return True
        else:
            return False

    def delete_player(self, lastname, firstname):
        if self.player_table.remove(
            (self.player_query.lastname == lastname)
            and (self.player_query.firstname == firstname)
        ):
            return True
        else:
            return False
