from models.tournament_model import *
from models.player_model import *
from  views.tournament_view import *
from models.round_model import Round

class TournamentController:
    def __init__(self, database) -> None:
        self.model = TournamentModel(database)
        self.view = TournamentView()
        self.player_model = PlayerModel(database)

    def get_tournaments_menu(self):
        while True:
            choice = self.view.display_tournaments_menu()
            match choice:
                case "1":
                    self.create_tournament()
                case "2":
                    self.list_tournaments()
                case "3":
                    self.get_tournament_menu()
                case "4":
                    self.update_tournament()
                case "5":
                    self.delete_tournament()
                case "b":
                    return
                case _other:
                    print("Choix invalide. Veuillez réessayer.")


    def get_tournament_menu(self):
        name = self.view.ask_name_tournament()
        tournament = self.model.get_tournament_by_name(name)

        while True:
            choice = self.view.display_tournament_menu(tournament)
            match choice:
                case "1":
                    self.enter_match_result(tournament)
                case "2":
                    self.list_results(tournament)
                case "3":
                    self.list_tournament_by_name(name)
                case "4":
                    self.update_tournament(name)
                case "5":
                    self.delete_tournament()
                case "b":
                    return
                case _other:
                    print("Choix invalide. Veuillez réessayer.")

    def create_tournament(self):
        name        = self.view.ask_name_tournament()
        if not information_is_ok(name):
            return self.view.ask_name_tournament()
        
        location    = self.view.ask_location_tournament()
        if not information_is_ok(location):
            return self.view.ask_location_tournament()
        
        description = self.view.ask_description_tournament()
        if not information_is_ok(description):
            return self.view.ask_description_tournament()
        
        nb_turns    = self.view.ask_nb_turns()
        if not ranking_is_ok(nb_turns):
            return self.view.ask_nb_turns()
        
        # players = [player.doc_id for player in self.player_model.player_table.all()]
        players = [{"lastname" : player.lastname, "firstname" : player.firstname, "rank" : player.rank, "score" : 0} for i, player in enumerate(self.player_model.get_all_players())]
        rounds_list = []
        rounds = Round(nb_turns)
        
        rounds.matches = rounds.generate_swiss_pairing(players)
        rounds = rounds.serialize_round()
        rounds_list.append(rounds)
        players_ids = [player.doc_id for player in self.player_model.player_table.all()]

        tournament = Tournament(name, location, rounds_list, players,description, nb_turns)

        self.model.create_tournament(tournament)
        self.view.success_creation_tournament()
        

    def list_tournaments(self):
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            tournaments = self.model.get_tournaments()
            self.view.display_tournaments(tournaments)


    def list_tournament_by_name(self,name):
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            tournament = self.model.get_tournament_by_name(name)
            self.view.display_tournament(tournament)


    def update_tournament(self, name=""):
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament() if name == "" else name
            update = self.view.ask_update_tournament()
        
            self.model.update_tournament(update, name)
        

    def delete_tournament(self):
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament()
        
            self.model.delete_tournament(name)
        
    def enter_match_result(self, tournament):
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            if tournament.end_date != "":
                self.view.forbidden_modify_tournament(tournament)
            else:
                self.view.display_tournament(tournament)
                
                for round in tournament.rounds:
                    if round["end_date"] == "":
                        matchs = round['matchs']
                        list_match = self.view.ask_results(matchs)
                        round['matchs'] = list_match
                        round['end_date'] = str(date.today())
                        round['end_hour'] =  str(datetime.now().time().strftime("%H:%M:%S"))

                if round["name"] == int(tournament.nb_turn):
                    tournament.end_date = str(date.today())
                    winner = self.get_tournament_results_by_tournament(tournament)[0]
                    self.view.tournament_is_over(winner)
                    self.model.update_round_tournament(tournament, tournament.name)
                else:
                    # création du prochain round
                    next_round = self.generate_next_round(round)
                    next_round.incremente_number()
                    round_serialized = next_round.serialize_round()
                    tournament.rounds.append(round_serialized)
                    self.model.update_round_tournament(tournament, tournament.name)
            
            

        
    def generate_next_round(self, previous_round):
        round = Round()
        matchs_previous_round = previous_round["matchs"]
        round.name = previous_round['name']
        round.matchs = round.generate_swiss_pairing_bis(matchs_previous_round)

        return round


    def get_tournament_results_by_tournament(self, tournament):
        last_round = tournament.rounds[-1]
        matchs = last_round["matchs"]
        tab_results = []
        for match in matchs:
            for players in match:
                for player in players:
                    tab_results.append(f'{player["lastname"]} {player["firstname"]} avec un score total de {player["score"]} points.')
         
        return tab_results



    def not_tournament_in_database(self):
        return True if self.model.not_tournament_in_database() else False



    def list_results(self, tournament):
        results = self.get_tournament_results_by_tournament(tournament)
        return self.view.display_tournament_results(results)
           
    
    
