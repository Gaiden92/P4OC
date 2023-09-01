from models.player_model import PlayerModel, Player
from views.player_view import PlayerView
from functions.functions import *

class PlayerController:
    def __init__(self, database ) -> None:
        self.model = PlayerModel(database)
        self.view = PlayerView()

    def get_players_menu(self):
        choice = self.view.display_players_menu()

        match choice:
            case "1":
                self.create_player()
            case "2":
                self.list_players()
            case "3":
                self.update_player()
            case "4":
                self.remove_player()
            case "b":
                return 
            case _other:
                print("Choix invalide. Veuillez réessayer.")

        


    def list_players(self):
        players = self.model.get_all_players()
        self.view.display_all_players(players)



    def create_player(self):

        lastname = self.view.ask_lastname()
        if not information_is_ok(lastname):
            return self.view.ask_lastname()
        
        firstname   = self.view.ask_firstname()    
        if not information_is_ok(firstname):
            return self.view.ask_firstname()
        
        gender      = self.view.ask_gender()
        if not gender_is_ok(gender):
            return self.view.ask_gender()
        
        birthdate   = self.view.ask_birth_date() 
        if not birth_is_ok(birthdate):
            return self.view.ask_birth_date()
        
        rank        = self.view.ask_rank()
        if not ranking_is_ok(rank):
            return self.view.ask_rank()

        
        self.model.create_player(Player(lastname, firstname, gender, birthdate, rank))
        self.view.success_add_player_view()
        self.add_player_continu()


    def add_player_continu(self):
        choice = self.view.ask_add_another_player() 
        if choice == "y":
            self.create_player()
            
    def update_player(self):
        
        lastname = self.view.ask_lastname()
        if not information_is_ok(lastname):
            return self.view.ask_lastname()
        
        firstname = self.view.ask_firstname()
        if not information_is_ok(firstname):
            return self.view.ask_firstname()
        
        column_number = self.view.ask_column_update()
        if not verify_column_to_update(column_number):
            return self.view.ask_column_update()
        
        update = self.view.ask_data_to_update(column_number)
        if not verify_data(column_number, update):
            return self.view.ask_data_to_update(column_number)

        column_name = get_column_name_by_number(column_number)

        if self.model.update_player(update, column_name, lastname, firstname):
            return self.view.success_editing_player_view()
        else:
            return self.view.failed_editing_player_view()
        

    def remove_player(self):
        lastname    = self.view.ask_lastname()
        if not information_is_ok(lastname):
            return self.view.ask_lastname()
        
        firstname   = self.view.ask_firstname()
        if not information_is_ok(firstname):
            return self.view.ask_firstname()
        
        lastname  = lastname.capitalize()
        firstname = firstname.capitalize()

        if self.is_exist(lastname, firstname):
            self.model.delete_player(lastname, firstname)
            self.view.success_remove_player_view()
        else:
            self.view.player_no_exist_view()
        

    def is_exist(self, lastname, firstname):
        return True if self.model.player_table.get((self.model.player_query.lastname == lastname) and (self.model.player_query.firstname == firstname)) else False