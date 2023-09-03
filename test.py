# import random
# from datetime import date, datetime

# class Match:
#     def __init__(self, player1, player2) -> None:
#         self.player1 = player1
#         self.player2 = player2

#         self.result = None



#     def match_serialized(self):
#         list_match =    (
#                             [self.player1],
#                             [self.player2]
#                         )

#         return list_match

# class Result:
#     def __init__(self, score1, score2) -> None:
#         self.score1 = score1
#         self.score2 = score2

# class Round:

#     def __init__(self, nb_round=0) -> None:
#         self.name                   = 1
#         self.nb_round               = nb_round
#         self.start_date             = str(date.today())
#         self.start_hour             = str(datetime.now().time().strftime("%H:%M:%S"))
#         self.end_date               = ""
#         self.end_hour               = ""

#         self.matchs                = []

#     def generate_swiss_pairing(self, list_players):
#         random.shuffle(list_players)

#         length_sorted_list = len(list_players)
        
#         index = 0
#         while index < length_sorted_list:
#             match = Match(list_players[index], list_players[index+1]).match_serialized()
#             self.matchs.append(match)
#             index+=2
#         return self.matchs

# def generate_swiss_pairs(list_players):
#         # Trie du tableau des joueurs
#         players_sorted_by_rank = sorted(list_players, key= lambda player : player['rank'], reverse=True)

#         lenght = len(players_sorted_by_rank)
#         mid = int(lenght / 2)

#         # génération du groupe inférieur et supérieur
#         sup_group = players_sorted_by_rank[0:mid]
#         inf_group = players_sorted_by_rank[mid:]

#         # création des pairs de match
#         matchs = []
#         for player1, player2 in zip(sup_group, inf_group):
#                 match = Match(player1, player2)
#                 print(match)
#                 matchs.append(match)
#         return matchs 
        



[
                        [
                            [
                                "Ouahid",
                                2.0
                            ],
                            [
                                "Akrey",
                                0.5
                            ]
                        ],
                        [
                            [
                                "Jean Claude",
                                0.5
                            ],
                            [
                                "Hedi",
                                1.0
                            ]
                        ]
                    ]





# players =  [ 
#                 {
#                 "lastname": "Fouchel",
#                 "firstname": "Sami",
#                 "rank": "5"
#                 },
#                 {
#                     "lastname": "Sekhaine",
#                     "firstname": "Thomas",
#                     "rank": "0"
#                 },
#                 {
#                     "lastname": "Couchy",
#                     "firstname": "Terry",
#                     "rank": "0"
#                 },
#                 {
#                     "lastname": "Agouassey",
#                     "firstname": "Akrey",
#                     "rank": "5"
#                 },
#                 {
#                     "lastname": "Pottier",
#                     "firstname": "Eddi",
#                     "rank": "3"
#                 },
#                 {
#                     "lastname": "Derfoufi",
#                     "firstname": "Morgan",
#                     "rank": "2"
#                 }
#         ]


# random.shuffle(players)
# rounde = Round()
# rounde.generate_swiss_pairing(players)
# print(rounde.matchs)


matchs = [
                        [
                            [
                                "Ouahid",
                                2.0
                            ],
                            [
                                "Akrey",
                                0.5
                            ]
                        ],
                        [
                            [
                                "Jean Claude",
                                0.5
                            ],
                            [
                                "Hedi",
                                1.0
                            ]
                        ]
                    ]

print(matchs[0])

for player in matchs:
    liste = matchs[0][0], matchs[0][1]
print(*liste)