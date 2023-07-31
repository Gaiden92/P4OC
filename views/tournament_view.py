from functions.functions import *
from datetime import date, datetime
class TournamentView:

    def display_tournaments_menu(self):
        # Display the Tournament menu #
        print("=== TOURNAMENTS MENU ===")
        print("1. Create new Tournament")
        print("2. List all Tournaments")
        print("3. Manage a Tournament")
        print("4. Edit a Tournament")
        print("5. Delete a Tournament")


        print("[b] Back to main menu")

        choice = input("Votre choix: ")

        return choice
    

    def display_tournament_menu(self, tournament):
        print(f"=== Manage Tournament : {tournament.name} ===")    
        print("1. Enter match results")
        print("2. See Tournament classement")
        print("3. List Tournament")
        print("4. Edit the Tournament")
        print("5. Delete the Tournament")

        print("[b] Back to Tournaments menu")

        choice = input("Votre choix: ")

        return choice

    def display_tournaments(self, tournaments):
        # Display all tournaments #
        print("== LISTE DES TOURNOIS ==")
        for tournament in tournaments:
            self.display_tournament(tournament)
            print("="*100)
            print()
    
    def display_tournament(self, tournament):
        # Display one tournament by his name #
        print(f"Nom : {tournament.name}")
        print(f"- Lieu : {tournament.localisation}")
        print(f"- Date de début : {tournament.date} ")
        print(f"- Date de fin : {tournament.end_date} ") if self.is_tournament_finish(tournament) else print(f"- Date de fin : tournoi en cours.. ")
        print(f"- Description : {tournament.description}" )
        print(f"Rondes : " )
        
        self.display_rounds(tournament.rounds)

                
    def display_rounds(self, rounds):
        for round in rounds:
            matchs = round['matchs']
            print(f" - Round n°{round['name']} : ") 
            for i, match in enumerate(matchs):
                print(f"    {i+1}. ", end="")
                for index, player in enumerate(match):
                    print("", end="") if index == 0 else print("", end="")
                    print(f'{player[0]["lastname"]} {player[0]["firstname"]} (points cumulés: {player[0]["score"]})', end="")
                    print(" VS ", end="") if index == 0 else print("", end="")
                    print(" (match terminé) ", end='') if len(player) >= 2 and index == 1 else print("", end='')
                print()
            print(f"    Ce round est terminé.") if self.is_round_finish(round) else print(f"    Round en cours.")


    def is_round_finish(self, round):
        return True if round['end_date'] != "" else False
  
    def is_tournament_finish(self, tournament):
        return True if tournament.end_date != "" else False

    def success_creation_tournament(self):
        print("Le tournoi a été crée avec succès")


    def ask_name_tournament(self):
        name = input("Entrer le nom du tournoi : ")
        
        return name if information_is_ok(name) else self.ask_name_tournament()

    def ask_location_tournament(self):
        location = input("Entrer le lieu du tournoi : ")

        return location if information_is_ok(location) else self.ask_location_tournament()
    
    def ask_description_tournament(self):
        description = input("Entrer la description du tournoi : ")
        
        return description if information_is_ok(description) else self.ask_description_tournament()

    def ask_nb_turns(self):
        nb_turns    = input("Entrer le nombre de tours du tournoi : ")

        return nb_turns if ranking_is_ok(nb_turns) else self.ask_nb_turns()
    
    
    def ask_update_tournament(self):
        update = input("Merci d'entrer le nouveau nom du tournoi : ")

        return update if information_is_ok(update) else self.ask_update_tournament()
    

    def ask_results(self, matchs_list):
        nb_match = 1
        while nb_match <= len(matchs_list):
            match = matchs_list[int(nb_match)-1]
                    
            print(f'Vous allez entrer les résultats du match n°{nb_match} : {match[0][0]["lastname"]} {match[0][0]["firstname"]} VS {match[1][0]["lastname"]} {match[1][0]["firstname"]}')
            for i,value in enumerate(match):
                
                score = input(f'Entrez le score du joueur {value[0]["lastname"]} : ')
                value[0]["score"] += float(score)

            nb_match+=1
        return matchs_list


    def tournament_is_over(self, winner):
        print("Le tournoi est fini ! ")
        print(f"le vainqueur du tournoi est : {winner}")

    def forbidden_modify_tournament(self, tournament):
        print(f'Le tournoi "{tournament.name}" est terminé. Vous ne pouvez plus entrer de résulats.')
    
    def display_not_tournament_in_db(self):
        print("Il n'y a aucun tournoi en base de donnée !")

    def display_tournament_results(self, results):
        for results in results:
            print(results)