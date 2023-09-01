from datetime import date
from tinydb import TinyDB, Query


class Tournament:

    def __init__(self, name:str, localisation:str, rounds:list, players:list, description: str, nb_turn=4, date=date.today(), end_date="") -> None:
        self.name           = name
        self.date           = str(date)
        self.localisation   = localisation
        self.nb_turn        = nb_turn
        self.rounds         = rounds
        self.players        = players
        self.description    = description
        self.end_date       = end_date
        

class TournamentModel:
    def __init__(self, database):
        self.db = TinyDB(database,indent=4, separators=(',', ': '))
        self.tournament_query = Query()
        self.tournament_table = self.db.table("tournois")
 


    def create_tournament(self, tournament):
        """
        Fonction permettant de créer un tournoi en base de donnée
        param = un objet Tournoi
        retourne = booleen
        """
        
        self.tournament_table.insert(
                                        {

                                            'name': tournament.name,
                                            'localisation': tournament.localisation,
                                            'nb_turn' : tournament.nb_turn,
                                            'players' : tournament.players,
                                            'rounds' : tournament.rounds,
                                            'description' : tournament.description,
                                            'date': tournament.date,
                                            'end_date' : tournament.end_date
                                        }
                                    )
        
    
    
    def get_tournaments(self):
        """
        Fonction permettant de récuperer tous les tournois en base de donnée
        param = un objet bdd
        retourne = booleen
        
        """
        tournaments = self.tournament_table.all()

        return [
                Tournament  ( 
                                tournament['name'], 
                                tournament['localisation'], 
                                tournament['rounds'], 
                                tournament['players'], 
                                tournament['description'],
                                tournament['nb_turn'],
                                tournament['date'],
                                tournament['end_date']
                            ) for tournament in tournaments
                ]
    
    
    def get_tournament_by_name(self, name)-> object:
        """
        Fonction permettant de récuperer un tournoi en base de donnée via son nom
        param = nom d'un tournoi
        retourne = objet tournament
        
        """
        tournament = self.tournament_table.get(self.tournament_query.name == name)
        if tournament:
            return  Tournament( 
                                tournament['name'], 
                                tournament['localisation'],
                                tournament['rounds'], 
                                tournament['players'], 
                                tournament['description'],
                                tournament['nb_turn'],
                                tournament['date'],
                                tournament['end_date']
                                )   
        else:
            return None
            
    def update_tournament(self, updates, name):
        """Modifier un tournoi via un nom """
        self.tournament_table.update({'name' : updates}, self.tournament_query.name == name)

    def update_rounds_tournament(self, updates ,name):
        """Modifier le round d'un tournoi via un nom """
        self.tournament_table.update({"rounds" : updates}, self.tournament_query.name == name)
        
    def update_round_tournament(self, updates, name):
        tournament = updates
        
        self.tournament_table.update(

                                        {
                                            'name': tournament.name,
                                            'localisation': tournament.localisation,
                                            'nb_turn' : tournament.nb_turn,
                                            'players' : tournament.players,
                                            'rounds' : tournament.rounds,
                                            'description' : tournament.description,
                                            'date': tournament.date,
                                            'end_date' : tournament.end_date
                                        }, 
                                        self.tournament_query.name == name
                                    )

    def delete_tournament(self, name):
        """Supprimer un tournoi via son nom"""
        self.tournament_table.remove(self.tournament_query.name == name)

    
    def get_rounds_by_tournament(self, name):
        tournament = self.tournament_table.get(self.tournament_query.name == name)
        if tournament:
            return tournament['rounds']
        else:
            return None
        
    def not_tournament_in_database(self):

        return len(self.tournament_table) == 0