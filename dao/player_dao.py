from tinydb import TinyDB
from tinydb import Query

from models.player import Player


class PlayerDao:
    """ "Une classe représentant le model de la classe <Player>.

    Attributs
    ----------
    database : str
        La base de donnée avec laquelle le model communiquera.

    """

    def __init__(self, database) -> None:
        """Construit tous les attributs nécessaires au model.

        Arguments:
            database -- La base de donnée avec laquelle le model communiquera.
        """
        self.db = TinyDB(database, indent=4, separators=(",", ": "))
        self.player_table = self.db.table("players")
        self.player_query = Query()

    def create_player(self, player: object) -> None:
        """La méthode permet d'ajouter un joueur en base de donnée.

        Arguments:
            player -- un objet <player>
        """
        player_serialize = player.serialize_player()
        self.player_table.insert(player_serialize)

    def get_all_players(self) -> list:
        """Récupère la liste de tous les joueurs en base de donnée.

        Returns:
            Tous les joueurs de la base de donnée sous forme d'une liste d'objet <player>
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
        """Récupère un joueur dont le nom et prénom on été indiqués en paramètres.

        Arguments:
            lastname -- le nom du joueur
            firstname -- le prénom du joueur

        Returns:
            Si le joueur est présent en base de donnée :
                un objet <player> contenant les informations du joueur
            Sinon :
                None
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
        """Mets à jour les données d'un joueur en effectuant une recherche par nom et prénom.

        Arguments:
            updates -- la nouvelle donnée
            column -- la colonne à mettre à jour (nom, prénom, age,...)
            lastname -- le nom du joueur
            firstname -- le prénom du joueur

        Retourne:
            bool : Si la mise à jour a été effectuée, la fonction retourne True
                   Sinon la fonction retourne False
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
        """Supprimer un joueur en effectuant une recherche par nom et prénom.

        Arguments:
            lastname -- le nom du joueur
            firstname -- le prénom du joueur

        Retourne:
            bool : Si la suppression a été effectuée, la fonction retourne True
                   Sinon la fonction retourne False
        """
        if self.player_table.remove(
            (self.player_query.lastname == lastname)
            and (self.player_query.firstname == firstname)
        ):
            return True
        else:
            return False

    def get_player_by_id(self, id: str) -> object:
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
