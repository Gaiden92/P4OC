rounds = [
                {
                    "name": 1,
                    "start_date": "2023-09-08",
                    "start_hour": "12:52:37",
                    "end_date": "2023-09-08",
                    "end_hour": "12:52:55",
                    "matchs": [
                        [
                            [
                                "Akrey",
                                1.0
                            ],
                            [
                                "Hedi",
                                0.0
                            ]
                        ],
                        [
                            [
                                "Jean Claude",
                                1.0
                            ],
                            [
                                "Ouahid",
                                0.0
                            ]
                        ]
                    ]
                },
                {
                    "name": 2,
                    "start_date": "2023-09-08",
                    "start_hour": "12:52:55",
                    "end_date": "2023-09-08",
                    "end_hour": "12:53:09",
                    "matchs": [
                        [
                            [
                                "Akrey",
                                1.0
                            ],
                            [
                                "Jean Claude",
                                2.0
                            ]
                        ],
                        [
                            [
                                "Hedi",
                                1.0
                            ],
                            [
                                "Ouahid",
                                0.0
                            ]
                        ]
                    ]
                },
                {
                    "name": 3,
                    "start_date": "2023-09-08",
                    "start_hour": "12:53:09",
                    "end_date": "",
                    "end_hour": "",
                    "matchs": [
                        [
                            [
                                "Jean Claude",
                                2.0
                            ],
                            [
                                "Hedi",
                                1.0
                            ]
                        ],
                        [
                            [
                                "Akrey",
                                1.0
                            ],
                            [
                                "Ouahid",
                                0.0
                            ]
                        ]
                    ]
                }
            ]




def already_played_together(rounds:list,players_names_list:list)->bool:
    for round in rounds:
        for match in round["matchs"]:
            player1_name = match[0][0]
            player2_name = match[1][0]
            players_names = [player1_name, player2_name]
            counter = 0

            for player in players_names_list:
                if player in players_names:
                    counter += 1
                    if counter == 2:
                        return True
                    
    return False



liste_trier = [['Akrey', 1.0], ['Hedi', 1.0], ['Ouahid', 1], ['Jean Claude', 1], ['Terry', 0.0], ['Doris', 0.0], ['Sami', 0.0], ['Nassima', 0.0]]

def match_pairing(list_trier):
    index_player1 = 0
    index_player2 = index_player1 + 1
    matchs = []
    while index_player1 < len(liste_trier):
        try:
            if already_played_together(rounds, [liste_trier[index_player1][0], liste_trier[index_player2][0]]):
                index_player2 += 1
        except:
            break
        else:
            matchs.append([liste_trier[index_player1], liste_trier[index_player2]])
            liste_trier.remove(liste_trier[index_player2])
            liste_trier.remove(liste_trier[index_player1])
            index_player2 = index_player1+1

    return matchs
        
print(match_pairing(liste_trier))



