from datetime import *


class Round:

    def __init__(self, nb_round=0) -> None:
        self.name                   = 1
        self.nb_round               = nb_round
        self.start_date             = str(date.today())
        self.start_hour             = str(datetime.now().time().strftime("%H:%M:%S"))
        self.end_date               = ""
        self.end_hour               = ""

        self.matchs                = []
        
    
    def incremente_number(self):
       self.name += 1

    def __str__(self) -> str:
        message = f"{self.name} :"

        return message


    def serialize_round(self):
        dict_round = {
                        "name" : self.name,
                        "start_date" : self.start_date,
                        "start_hour" : self.start_hour,
                        "end_date" : self.end_date,
                        "end_hour" : self.end_hour,
                        "matchs"    : self.matchs
                    }
    
        return dict_round
    

    
    def generate_swiss_pairing(self, list_players):
        liste_trier = sorted(list_players, key= lambda player : int(player["rank"]), reverse=True)

        taille = len(liste_trier)
        coupe = round(taille / 2)
        mid_inf = liste_trier[0:coupe]
        mid_sup = liste_trier[coupe:taille] 
        
        for player1, player2 in zip(mid_inf, mid_sup):
            match = Match(player1, player2).match_serialized()
            
            self.matchs.append(match)

        return self.matchs

    def generate_swiss_pairing_bis(self, matchs):
        list_players = []
        for match in matchs:
            for players in match:
                for player in players:
                    list_players.append(player)
        

        liste_trier_par_score = sorted(list_players, key= lambda player : float(player["score"]), reverse=True)

        index = 0
        while index < len(liste_trier_par_score):
            player1 = liste_trier_par_score[index]
            player2 = liste_trier_par_score[index+1]
            match = Match(player1, player2).match_serialized()
            
            self.matchs.append(match)
            index += 2


        return self.matchs
        

class Match:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2

        self.result = None
    
    def match_serialized(self):
        list_match =    (
                            [self.player1],
                            [self.player2]
                        )

        return list_match
                            
                        

class Result:
    def __init__(self, score1, score2) -> None:
        self.score1 = score1
        self.score2 = score2




