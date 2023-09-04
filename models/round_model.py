from datetime import *
from random import shuffle
from functions import already_played_together
class Round:

    def __init__(self, name=0) -> None:
        self.name                   = name
        self.start_date             = str(date.today())
        self.start_hour             = str(datetime.now().time().strftime("%H:%M:%S"))
        self.end_date               = ""
        self.end_hour               = ""

        self.matchs                = []
        
    


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
    

    
    def generate_first_round(self, list_players):
        shuffle(list_players)
        length_sorted_list = len(list_players)
        
        index = 0
        while index < length_sorted_list:
            score1 = 0
            score2 = 0
            match = Match([list_players[index].firstname, score1], [list_players[index+1].firstname, score2]).match_serialized()
            self.matchs.append(match)
            index+=2

        return self.matchs
    
    
    
        

class Match:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2

        self.result = None
    
    def match_serialized(self):
        list_match =    (
                            self.player1,
                            self.player2
                        )

        return list_match
                            
                        

class Result:
    def __init__(self, score1=0, score2=0) -> None:
        self.score1 = score1
        self.score2 = score2


    def serialized(self):
        result =    {
                        "Score1" : self.score1,
                        "Score2" : self.score2 
                    }
        return result
