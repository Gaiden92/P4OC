from models.match_model import MatchModel
import random as r


class MatchController:
    def __init__(self, players:list) -> None:
        self.players = players
        self.model  = MatchModel()


    def generate_match(self):
        """
        Fonction permettant de générer les scores d'un match aléatoirement.
        paramètres : liste contenant 2 dictionnaires (2 joueurs)
        retourne   : liste contenant 2 dictionnaires (2 joueurs) 
        """
        for index, player in enumerate(self.players):
            score = r.randint(0,1)
            player['score'] = score

        return self.players
    
    
    def match_result(self, list_players:list):
        """
        Fonction permettant de connaitre le gagnant et le perdant d'un match
        paramètres : liste de 2 joueurs
        retourne   : 2 chaine de caractère
        """
        
        if self.is_there_a_winner(list_players):
            liste_trier = sorted(list_players, key=lambda player : player['score'], reverse=True)
            liste_trier[0]["winner"] =  True
            liste_trier[1]["winner"] = False
            
            return liste_trier
        else:
            for e in list_players:
                e["winner"] = False

            return list_players
        
    def is_there_a_winner(self, list_players:list):
        """"
        Fonction permettant de savoir s'il y a un gagnant
        paramètres : liste de 2 joueurs
        retourne   : 2 chaine de caractère
        """        
        
        if list_players[0]["score"] != list_players[1]["score"]:
            return True
        else:

            return False

