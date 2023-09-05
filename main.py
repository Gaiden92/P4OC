from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
import tableprint  as tp

def main():
    database = "db.json"
    tournament_controller = TournamentController(database)
    player_controller = PlayerController(database)

    while True:
        tp.banner("MAIN MENU          ")
        print("1. Manage Tournaments")
        print("2. Manage Players")
        print("3. Reports")
        print("[q] Exit programm")

        choice = input("Votre choix: ")
        match choice:
            case  "1":
                tournament_controller.get_tournaments_menu()
            case  "2":
                player_controller.get_players_menu()
            case "3":
                pass
            case "q":
                exit()
            case _:
                print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()