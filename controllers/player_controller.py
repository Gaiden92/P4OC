from models.player_model import PlayerModel, Player
from views.player_view import PlayerView
import functions as f


class PlayerController:
    """ "Une classe représentant le controller de la classe <Player>.

    Attributs
    ----------
    database : str
        La base de donnée à gérer

    """

    def __init__(self, database: str) -> None:
        """Construit tous les attributs nécessaires de la classe.

        Arguments:
            database -- La base de donnée à gérer
        """
        self.model = PlayerModel(database)
        self.view = PlayerView()

    def get_players_menu(self) -> None:
        """Contrôle les entrées du menu joueur"""
        choice = self.view.display_players_menu()

        match choice:
            case "1":
                self.create_player()
            case "2":
                self.list_player_controller()
            case "3":
                self.list_players_controller()
            case "4":
                self.update_player()
            case "5":
                self.remove_player()
            case "b":
                return
            case _:
                self.view.invalid_choice()

    def list_player_controller(self) -> None:
        """Contrôle si un joueur est présent dans la base de donnée"""
        lastname = self.view.ask_lastname()
        firstname = self.view.ask_firstname()
        player = self.model.get_player(lastname, firstname)
        if player:
            self.view.display_player_view(player)
        else:
            self.view.no_existing_players_view()

    def list_players_controller(self) -> None:
        """Contrôle si un/des joueur(s) est/sont présent(s) dans la base de donnée"""
        players = self.model.get_all_players()
        if players:
            sorted_list_players = sorted(players, key=lambda player: player.lastname)
            self.view.display_all_players(sorted_list_players)
        else:
            self.view.no_existing_players_view()

    def create_player(self) -> None:
        """Contrôle l'intégralité des données utilisateurs entrées lors de la création
            d'un joueur.

        Valeurs de retour:
            Si une condition est fausse :
                La vue relative au contrôle des données ayant échoué.
            Si toutes les conditions sont vraies, le <PlayerModel> est appelé pour l'enregistrement du joueur
            en base de donnée.
        """
        lastname = self.view.ask_lastname()
        if not f.information_is_ok(lastname):
            return self.view.ask_lastname()

        firstname = self.view.ask_firstname()
        if not f.information_is_ok(firstname):
            return self.view.ask_firstname()

        gender = self.view.ask_gender()
        if not f.gender_is_ok(gender):
            return self.view.ask_gender()

        birthdate = self.view.ask_birth_date()
        if not f.birth_is_ok(birthdate):
            return self.view.ask_birth_date()

        player = Player("", lastname, firstname, gender, birthdate)
        if self.model.get_player(player.lastname, player.firstname):
            self.view.player_already_exist_view(player)
        else:
            self.model.create_player(player)
            self.view.success_add_player_view()
        self.add_player_continu()

    def add_player_continu(self) -> None:
        """Contrôle le choix de l'utilisateur s'il souhaite continuait à
        ajouter des joueurs.
        """
        choice = self.view.ask_add_another_player()
        if choice == "y":
            self.create_player()

    def update_player(self) -> None:
        """Contrôle l'intégralité des données utilisateurs entrées lors de la modification
            d'un joueur.

        Valeurs de retour:
            Si une condition est fausse :
                La vue relative au contrôle des données ayant échoué.
            Si toutes les conditions sont vraies, le <PlayerModel> est appelé pour la modification du joueur
            en base de donnée et la vue nécessaire est appelée pour informer l'utilisateur.
        """
        lastname = self.view.ask_lastname()
        if not f.information_is_ok(lastname):
            return self.view.ask_lastname()

        firstname = self.view.ask_firstname()
        if not f.information_is_ok(firstname):
            return self.view.ask_firstname()

        column_number = self.view.ask_column_update()
        if not f.verify_column_to_update(column_number):
            return self.view.ask_column_update()

        update = self.view.ask_data(column_number)
        if not f.verify_data(column_number, update):
            return self.view.ask_data(column_number)

        column_name = f.get_column_name_by_number(column_number)

        if self.model.update_player(update, column_name, lastname, firstname):
            return self.view.success_editing_player_view()
        else:
            return self.view.failed_editing_player_view()

    def remove_player(self) -> None:
        """Contrôle l'intégralité des données utilisateurs entrées lors de la suppression
            d'un joueur.

        Valeurs de retour:
            Si une condition est fausse :
                La vue relative au contrôle des données ayant échoué.
            Si toutes les conditions sont vraies, le <PlayerModel> est appelé pour la suppression du joueur
            en base de donnée et la vue nécessaire est appelée pour informer l'utilisateur.
        """
        lastname = self.view.ask_lastname()
        if not f.information_is_ok(lastname):
            return self.view.ask_lastname()

        firstname = self.view.ask_firstname()
        if not f.information_is_ok(firstname):
            return self.view.ask_firstname()

        lastname = lastname.capitalize()
        firstname = firstname.capitalize()

        if self.model.delete_player(lastname, firstname):
            self.view.success_remove_player_view()
        else:
            self.view.player_no_exist_view()
