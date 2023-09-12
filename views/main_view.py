import tableprint as tp

from .report_view import ReportView
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController


class MainView:
    def __init__(self, database) -> None:
        self.db = database
        self.tournament_controller = TournamentController(database)
        self.player_controller = PlayerController(database)
        self.report_view = ReportView(self.db)

    def display_main_menu(self):
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
