import tableprint as tp

from .report_view import ReportView
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController


class MainView:
    """A class representing the view of the main programm"""

    def __init__(self, database: str) -> None:
        """Constructs all necessary attributes of the class.

        Arguments:
            database -- The database to manage
        """
        self.db = database
        self.tournament_controller = TournamentController(database)
        self.player_controller = PlayerController(database)
        self.report_view = ReportView(database)

    def display_main_menu(self) -> None:
        """Displaying the main menu"""
        while True:
            tp.banner("MAIN MENU          ")
            print("1. Manage Tournaments")
            print("2. Manage Players")
            print("3. Reports")
            print("[q] Exit programm")

            choice = input("Votre choix: ")
            match choice:
                case "1":
                    self.tournament_controller.get_tournaments_menu()
                case "2":
                    self.player_controller.get_players_menu()
                case "3":
                    self.report_view.display_report_view()
                case "q":
                    exit()
                case _:
                    print("Choix invalide. Veuillez réessayer.")
