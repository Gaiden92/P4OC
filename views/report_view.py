import tableprint as tp

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


class ReportView:
    def __init__(self, database) -> None:
        self.db = database
        self.player_controller = PlayerController(database)
        self.tournament_controller = TournamentController(database)

    def display_report_view(self):
        while True:
            tp.banner("Report view          ")
            print("1. List all players by name")
            print("2. List all tournaments")
            print("3. List name and dates for one tournament")
            print("4. List of tournament players by name")
            print("5. List of all tournament rounds and all round matches")
            print("[b] Back to main menu")

            choice = input("Votre choix: ")
            match choice:
                case "1":
                    self.player_controller.list_players_controller()
                case "2":
                    self.tournament_controller.list_tournaments()
                case "3":
                    self.tournament_controller.list_tournament_by_name()
                case "4":
                    self.tournament_controller.get_all_tournament_players()
                case "5":
                    self.tournament_controller.list_round_and_match()
                case "b":
                    return
                case _:
                    print("Choix invalide. Veuillez réessayer.")
