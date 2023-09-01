from functions.functions import *

class PlayerView:
    
    def display_players_menu(self)->str:
        """Affiche le menu de gestion des joueurs

        Returns:
            str: le choix de l'utilisateur.
        """
        print("=== PLAYERS MENU ===")
        print("1. Create new player")
        print("2. List all players")
        print("3. Edit existing player")
        print("4. Remove player")


        print("[b] Back to main menu")

        choice = input("Votre choix: ")

        return choice  
#         

    def display_all_players(self, players:list)->None:
        """Affiche la liste de tous les joueurs présent en base de donnée.

        Args:
            players (list): une liste d'objets <joueur>.
        """
        nb_player = len(players)
        print(f"Liste des joueurs ({nb_player}): ")
        for player in players:
            print(player)
            

    def get_player(self, player:object)->None:
        """Affiche les caractéristiques d'un joueur présent en base de donnée.

        Args:
            player (object): le joueur dont les caractéristiques doivent être affichés
        """
        print(f"Voici les infos du joueurs {player.lastname} {player.firstname} : ")
        print(player)

    
    
    def ask_lastname(self)->str or function:
        """Demande à l'utilisateur son nom de famille.

        Returns:
            str or function: le nom si entrée valide sinon la fonction est rappellée.
        """
        lastname = input("Quel est le nom du joueur? ")

        return lastname  if information_is_ok(lastname) else self.ask_lastname()
            
        
    def ask_firstname(self)->str or function:
        """Demande à l'utilisateur son prénom

        Returns:
            str or function: le prénom si entrée valide sinon la fonction est rappellée.
        """
        firstname = input("Quel est le prénom du joueur? ")

        return firstname if information_is_ok(firstname) else self.ask_firstname()

    def ask_gender(self)->str or function:
        """Demande à l'utilisateur son genre

        Returns:
            str or function: le genre si entrée valide sinon la fonction est rappellée.
        """
        gender = input("Quel est votre sexe (masculin ou féminin) ? \n [H/F]")
        
        return gender if gender_is_ok(gender) else self.ask_gender()


    def ask_birth_date(self)->str or function:
        """Demande à l'utilisateur sa date de naissance

        Returns:
            str or function: la date de naissance si entrée valide sinon la fonction est rappellée.
        """
        birth_date = input("Quel est votre date de naissance (format dd-mm-yyyy) ? ")
    
        return birth_date if birth_is_ok(birth_date) else self.ask_birth_date()
    
    def ask_rank(self)->str or function:
        """Demande à l'utilisateur son classement

        Returns:
            str or function: le classement si entrée valide sinon la fonction est rappellée.
        """
        rank = input("Quel est le rang du joueur ? ")

        return rank if ranking_is_ok(rank) else self.ask_rank()


    def ask_add_another_player(self)->str or function:
        """Demande à l'utilisateur s'il souhaite ajouter un nouveau joueur

        Returns:
            str or function: le choix de l'utilisateur si entrée valide sinon la fonction est rappellée.
        """
        continu =  input("Voulez-vous ajouter un autre joueur ? [y/n] ")

        return continu if verify_continu(continu) else self.ask_add_another_player() 
    

    def ask_column_update(self)->str or function:
        """Demande à l'utilisateur quelle caractéristique du joueur modifier

        Returns:
            str or function: le choix de l'utilisateur si entrée valide sinon la fonction est rappellée.
        """
        column = input("Quelle colonne souhaitez vous modifier : \n 1. Nom\n 2. Prénom\n 3. Genre\n 4. Birthdate\n 5. Rank`\n ")
    
        return column if verify_column_to_update(column) else self.ask_column_update()
    

    def ask_data(self, column_name:str)->str or function:
        """Demande à l'utilisateur d'entrer la nouvelle caractéristique du joueur

        Arguments:
            column_name -- la caractéristique à modifier
             
        Returns:
            str or function: le choix de l'utilisateur si entrée valide sinon la fonction est rappellée.

        """
        data = input("Entrer la nouvelle donnée :  ")
        return data if verify_data(column_name, data ) else self.ask_data(column_name)
            
    def success_add_player_view(self)->None:
        """Informe l'utilisateur que le joueur a été créé avec succès
        """
        print(f"Le joueur a été ajouté avec succès ! ")

    def success_editing_player_view(self)->None:
        """Informe l'utilisateur que le joueur a été modifier avec succès
        """
        print(f"Le joueur a été modifié avec succès ! ")

    def failed_editing_player_view(self)->None:
        """Informe l'utilisateur que le joueur n'a pas pu être modifié
        """
        print(f"Le joueur n'a pas pu être modifié car il n'existe pas en base de donnée.")

    def success_remove_player_view(self)->None:
        """Informe l'utilisateur que le joueur a été supprimé avec succès
        """
        print(f"Le joueur a été supprimé de la base de donnée avec succès  ! ")
        
    def player_no_exist_view(self)->None:
        """Informe l'utilisateur que le joueur demandé n'existe pas en base de donnée
        """
        print(f"Le joueur n'existe pas en base de donnée ! ")

    def no_existing_players_view(self)->None:
        """Informe l'utilisateur qu'aucun joueur n'existe en base de donnée
        """
        print("Il n'y a aucun joueur en base de donnée ! ")