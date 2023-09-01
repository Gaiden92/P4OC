from functions.functions import *

class PlayerView:
    
    def display_players_menu(self):
        print("=== PLAYERS MENU ===")
        print("1. Create new player")
        print("2. List all players")
        print("3. Edit existing player")
        print("4. Remove player")


        print("[b] Back to main menu")

        choice = input("Votre choix: ")

        return choice  
#         

    def display_all_players(self, players):
        nb_player = len(players)
        print(f"Liste des joueurs ({nb_player}): ")
        for player in players:
            print(player)
            
        

    def get_player(self, player):
        print(f"Voici les infos du joueurs {player.lastname} {player.firstname} : ")
        print(player)

    
    
    def ask_lastname(self):
        lastname = input("Quel est le nom du joueur? ")

        return lastname  if information_is_ok(lastname) else self.ask_lastname()
            
        
    def ask_firstname(self):
        firstname = input("Quel est le prénom du joueur? ")

        return firstname if information_is_ok(firstname) else self.ask_firstname()

    def ask_gender(self):
        gender = input("Quel est votre sexe (masculin ou féminin) ? \n [H/F]")
        
        return gender if gender_is_ok(gender) else self.ask_gender()


    def ask_birth_date(self):
        birth_date = input("Quel est votre date de naissance (format dd-mm-yyyy) ? ")
    
        return birth_date if birth_is_ok(birth_date) else self.ask_birth_date()
    
    def ask_rank(self):
        rank = input("Quel est le rang du joueur ? ")

        return rank if ranking_is_ok(rank) else self.ask_rank()


    def ask_add_another_player(self):
        continu =  input("Voulez-vous ajouter un autre joueur ? [y/n] ")

        return continu if verify_continu(continu) else self.ask_add_another_player() 
    

    def ask_column_update(self):
        column = input("Quelle colonne souhaitez vous modifier : \n 1. Nom\n 2. Prénom\n 3. Genre\n 4. Birthdate\n 5. Rank`\n ")
    
        return column if verify_column_to_update(column) else self.ask_column_update()
    

    def ask_data_to_update(self, column_name):
        data = input("Entrer la nouvelle donnée :  ")
        return data if verify_data(column_name, data ) else self.ask_data_to_update(column_name)
            
    def success_add_player_view(self):
        print(f"Le joueur a été ajouté avec succès ! ")

    def success_editing_player_view(self):
        print(f"Le joueur a été modifié avec succès ! ")

    def failed_editing_player_view(self):
        print(f"Le joueur n'a pas pu être modifié.")

    def success_remove_player_view(self):
        print(f"Le joueur a été supprimé avec succès ! ")

    def succes_remove_player_view(self):
        print(f"Le joueur a été supprimé de la base de donnée avec succès  ! ")
        
    def player_no_exist_view(self):
        print(f"Le joueur n'existe pas en base de donnée ! ")