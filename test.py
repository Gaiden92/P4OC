import random

class Match:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2

        self.result = None

class Result:
    def __init__(self, score1, score2) -> None:
        self.score1 = score1
        self.score2 = score2

players =  [ 
                {
                "lastname": "Fouchel",
                "firstname": "Sami",
                "rank": "5"
                },
                {
                    "lastname": "Sekhaine",
                    "firstname": "Thomas",
                    "rank": "0"
                },
                {
                    "lastname": "Couchy",
                    "firstname": "Terry",
                    "rank": "0"
                },
                {
                    "lastname": "Agouassey",
                    "firstname": "Akrey",
                    "rank": "5"
                },
                {
                    "lastname": "Pottier",
                    "firstname": "Eddi",
                    "rank": "3"
                },
                {
                    "lastname": "Derfoufi",
                    "firstname": "Morgan",
                    "rank": "2"
                }
        ]

def generate_swiss_pairs(list_players):
        # Trie du tableau des joueurs
        players_sorted_by_rank = sorted(list_players, key= lambda player : player['rank'], reverse=True)

        lenght = len(players_sorted_by_rank)
        mid = int(lenght / 2)

        # génération du groupe inférieur et supérieur
        sup_group = players_sorted_by_rank[0:mid]
        inf_group = players_sorted_by_rank[mid:]

        # création des pairs de match
        matchs = []
        for player1, player2 in zip(sup_group, inf_group):
                match = Match(player1, player2)
                print(match)
                matchs.append(match)
        return matchs 
        

list_des_matchs = generate_swiss_pairs(players)

