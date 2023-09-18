from dao.player_dao import PlayerDao
from models.player import Player
from views.player_view import PlayerView
import functions as f


class PlayerController:
    """A class representing the controller of the <Player> class."""

    def __init__(self, database: str) -> None:
        """Constructs all necessary attributes of the class.

        Arguments:
            database -- The database to manage
        """
        self.dao = PlayerDao(database)
        self.view = PlayerView()

    def get_players_menu(self) -> None:
        """Controls player menu user's entries"""
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
        """Check if a player is present in the database"""
        lastname = self.view.ask_lastname()
        firstname = self.view.ask_firstname()
        player = self.dao.get_player(lastname, firstname)
        if player:
            self.view.display_player_view(player)
        else:
            self.view.no_existing_players_view()

    def list_players_controller(self) -> None:
        """Checks if at least one player is present in the database"""
        players = self.dao.get_all_players()
        if players:
            sorted_list_players = sorted(players, key=lambda player: player.lastname)
            self.view.display_all_players(sorted_list_players)
        else:
            self.view.no_existing_players_view()

    def create_player(self) -> None:
        """Controls all user data entered during creation of a player.

        Returns:
            if False :
                the failed data check view.
            if True :
                the <PlayerDao> is called for player registration
                    in the database.
        """
        id_player = self.view.ask_id()

        if self.dao.get_player_by_id(id_player):
            self.view.id_already_exist_view(id_player)
            return self.create_player()

        if not f.id_is_ok(id_player):
            return self.view.ask_id()

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

        player = Player(id_player, lastname, firstname, gender, birthdate)
        if self.dao.get_player(player.lastname, player.firstname):
            self.view.player_already_exist_view(player)
        else:
            self.dao.create_player(player)
            self.view.success_add_player_view()
        self.add_player_continu()

    def add_player_continu(self) -> None:
        """Controls all user data entered during creation
        of a player.
        """
        choice = self.view.ask_add_another_player()
        if choice == "y":
            self.create_player()

    def update_player(self) -> None:
        """Controls the completeness of user data entered during modification
            of a player.

        Returns:
            If a condition is false:
                The failed data check view.
            If all conditions are true, the <PlayerDao> is called for player modification
                in the database and the necessary view is called to inform the user.
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

        if self.dao.update_player(update, column_name, lastname, firstname):
            return self.view.success_editing_player_view()
        else:
            return self.view.failed_editing_player_view()

    def remove_player(self) -> None:
        """Checks the completeness of user data entered when deleting
            of a player.

        Returns:
            If a condition is false:
                the failed data check view.
            If all conditions are true:
                the <PlayerDao> is called for player deletion
                in the database and the necessary view is called to inform the user.
        """
        lastname = self.view.ask_lastname()
        if not f.information_is_ok(lastname):
            return self.view.ask_lastname()

        firstname = self.view.ask_firstname()
        if not f.information_is_ok(firstname):
            return self.view.ask_firstname()

        lastname = lastname.capitalize()
        firstname = firstname.capitalize()

        if self.dao.delete_player(lastname, firstname):
            self.view.success_remove_player_view()
        else:
            self.view.player_no_exist_view()
