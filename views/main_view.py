import tableprint  as tp
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController

class MainView:
    def __init__(self, database) -> None:
        self.db = "db.json"
        self.tournament_controller = TournamentController(database)
        self.player_controller = PlayerController(database)


    def display_main_programm_view(self):
        while True:
            tp.banner("MAIN MENU          ")
            print("1. Manage Tournaments")
            print("2. Manage Players")
            print("3. Reports")
            print("[q] Exit programm")

            choice = input("Votre choix: ")
            match choice:
                case  "1":
                    self.tournament_controller.get_tournaments_menu()
                case  "2":
                    self.player_controller.get_players_menu()
                case "3":
                    pass
                case "q":
                    exit()
                case _:
                    print("Choix invalide. Veuillez réessayer.")
