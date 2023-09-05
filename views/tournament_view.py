from functions import *
from datetime import date, datetime
import tableprint as tp
import random as r
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
        tp.banner("LISTE DES TOURNOIS                                       ", width=99)
        for tournament in tournaments:
            self.display_tournament(tournament)
            print("="*100)
            print()
    
    def display_tournament(self, tournament):
        header = tp.header(["Nom", "Lieu", "Date de début", "Date de fin", "Description"], width=17)
        bottom = tp.bottom(5, 17)
        print(header)
        # Display one tournament by his name #
        row = tp.row(
                        [   
                            tournament.name, 
                            tournament.localisation,
                            tournament.date,
                            tournament.end_date if self.is_tournament_finish(tournament) else "en cours", 
                            tournament.description
                         ],
                         17
                    )
        print(row)
        print(bottom)
        self.display_rounds(tournament.rounds)

                
    def display_rounds(self, rounds):
        for round in rounds:
            matchs = round['matchs']
            status = "terminé" if self.is_round_finish(round) else "en cours"
            tp.banner(f'RONDE N°{round["name"]} ({status})                                      ', 99)
            header = tp.header(["Match"], 97, align="center")
            print(header)
            for match in matchs:
                match_str = ""
                colors = ["blancs", "noirs"]
                for index, informations_player in enumerate(match):
                    
                    player_name = informations_player[0]
                    player_score = informations_player[1]
                    player_chess_piece_color = r.choice(colors)
                    if index == len(match)-1:
                        match_str += f"{player_name} ({player_chess_piece_color})"
                    else:
                        
                        match_str += f"{player_name} ({player_chess_piece_color}) VS "
                    colors.remove(player_chess_piece_color)

                row = tp.row(match_str.split(","), 97, align="center")
                print(row)                   
            
            print(tp.bottom(1, 97))


    def is_round_finish(self, round):
        return True if round['end_date'] != "" else False
  
    def is_tournament_finish(self, tournament):
        return True if tournament.end_date != "" else False

    def success_creation_tournament(self):
        print("Le tournoi a été crée avec succès ! ")

    def failed_creation_tournament(self):
        print("La création du tournoi a échoué ! ")

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
            player = matchs_list[int(nb_match)-1]
            player1 = player[0]
            player2 = player[1]
            player1_name = player1[0]
            player2_name = player2[0]

            print(f'Vous allez entrer les résultats du match n°{nb_match} : {player1_name} VS {player2_name} ')
            for index,value in enumerate(player):
                
                score = input(f'Entrez le score du joueur {player[index][0]} : ')

                player[index][1] += float(score)

            nb_match+=1
        return matchs_list


    def tournament_is_over(self, winner):
        print("Le tournoi est fini ! ")
        print(f'le vainqueur du tournoi est : {winner["name"]} avec un score final de {winner["score"]}')

    def forbidden_modify_tournament(self, tournament):
        print(f'Le tournoi "{tournament.name}" est terminé. Vous ne pouvez plus entrer de résulats.')
    
    def display_not_tournament_in_db(self):
        print("Il n'y a aucun tournoi en base de donnée !")

    def display_tournament_results(self, results):
        header = tp.header(["Nom", "Score", "Classement"], 15)
        print(header)
        for index, player in enumerate(results):
                print(tp.row([player["name"], player["score"], index+1 ],15))
        print(tp.bottom(3,15))