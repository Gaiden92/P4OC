from models.player_model import PlayerModel, Player
from views.player_view import PlayerView
import functions as f

class PlayerController:
    def __init__(self, database)->None:
        self.model = PlayerModel(database)
        self.view = PlayerView()

    def get_players_menu(self)->None:
        """Contrôle les entrées du menu joueur
        """
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
            case _other:
                print("Choix invalide. Veuillez réessayer.")

        
    def list_player_controller(self)->None:
        """Contrôle si un joueur est présent dans la base de donnée
        """
        lastname = self.view.ask_lastname()
        firstname = self.view.ask_firstname()
        player = self.model.get_player(lastname, firstname)
        if player:
            self.view.display_player_view(player)
        else:
            self.view.no_existing_players_view()

    def list_players_controller(self)->None :
        """Contrôle si un/des joueur(s) est/sont présent(s) dans la base de donnée
        """
        players = self.model.get_all_players()
        if players:
            sorted_list_players = sorted(players, key= lambda player : player.lastname)
            self.view.display_all_players(sorted_list_players)
        else:
            self.view.no_existing_players_view()


    def create_player(self):
        
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
        
        rank = self.view.ask_rank()
        if not f.ranking_is_ok(rank):
            return self.view.ask_rank()

        
        self.model.create_player(Player("", lastname, firstname, gender, birthdate, rank))
        self.view.success_add_player_view()
        self.add_player_continu()


    def add_player_continu(self):
        choice = self.view.ask_add_another_player() 
        if choice == "y":
            self.create_player()
            
    def update_player(self):
        
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

        if self.model.update_player(update, column_name, lastname, firstname):
            return self.view.success_editing_player_view()
        else:
            return self.view.failed_editing_player_view()
        

    def remove_player(self):
        lastname = self.view.ask_lastname()
        if not f.information_is_ok(lastname):
            return self.view.ask_lastname()
        
        firstname = self.view.ask_firstname()
        if not f.information_is_ok(firstname):
            return self.view.ask_firstname()
        
        lastname = lastname.capitalize()
        firstname = firstname.capitalize()

        if self.model.delete_player(lastname, firstname):
            self.view.success_remove_player_view()
        else:
            self.view.player_no_exist_view()
        