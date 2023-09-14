import random

import functions as f
import tableprint as tp


class TournamentView:
    def display_tournaments_menu(self):
        tp.banner("TOURNAMENTS MENU       ")
        print("1. Create new Tournament")
        print("2. List all Tournaments")
        print("3. Manage a Tournament")
        print("4. Edit a Tournament")
        print("5. Delete a Tournament")

        print("[b] Back to main menu")

        choice = input("Votre choix: ")

        return choice

    def display_tournament_menu(self, tournament):
        tp.banner(f"Manage : {tournament.name}     ", 20)
        print("1. Enter match results")
        print("2. See Tournament classement")
        print("3. List Tournament")
        print("4. Edit the Tournament")
        print("5. Delete the Tournament")
        print("6. List round tournament")

        print("[b] Back to Tournaments menu")

        choice = input("Votre choix: ")

        return choice

    def display_tournaments(self, tournaments):
        # Display all tournaments #

        for tournament in tournaments:
            self.display_tournament(tournament)
            print()

    def display_tournament(self, tournament):
        header = tp.header(
            [
                "Nom",
                "Lieu",
                "Date de début",
                "Date de fin",
                "Ronde en cours",
                "Description",
            ],
            width=20,
        )
        bottom = tp.bottom(6, 20)
        print(header)
        # Display one tournament by his name #
        row = tp.row(
            [
                tournament.name,
                tournament.localisation,
                tournament.date,
                tournament.end_date
                if self.is_tournament_finish(tournament)
                else "en cours",
                tournament.current_round,
                tournament.description,
            ],
            20,
        )
        print(row)
        print(bottom)

    # def display_rounds(self, rounds):
    #     for round in rounds:
    #         matchs = round["matchs"]
    #         status = "terminé" if self.is_round_finish(round) else "en cours"
    #         tp.banner(
    #             f'RONDE N°{round["name"]} ({status})                                                 ',
    #             120,
    #         )
    #         header = tp.header(["Matchs"], 118, align="center")
    #         print(header)
    #         for match in matchs:
    #             match_str = ""
    #             colors = ["blancs", "noirs"]
    #             for index, informations_player in enumerate(match):
    #                 player_name = informations_player[0]
    #                 player_score = informations_player[1]
    #                 player_chess_piece_color = random.choice(colors)
    #                 if index == len(match) - 1:
    #                     match_str += f"{player_name} {player_score} ({player_chess_piece_color})"
    #                 else:
    #                     match_str += f"{player_name} {player_score} ({player_chess_piece_color}) VS "
    #                 colors.remove(player_chess_piece_color)
    #             row = tp.row(match_str.split(","), 118, align="center")
    #             print(row)
    #         print(tp.bottom(1, 118))

    def display_round(self, rounds: list) -> None:
        for index, round in enumerate(rounds):
            if round["end_date"] == "":
                banner = f"Tour n°{index+1} - en cours                                          "
            else:
                banner = f"Tour n°{index+1} - terminé                                           "
            tp.banner(banner, 103)
            header = tp.header(
                [
                    "Match",
                    "Player 1",
                    "Couleur P1",
                    "",
                    "Player 2",
                    "Couleur P2",
                    "Score P1",
                    "Score P2",
                ],
                15,
            )
            bottom = tp.bottom(8, 15)

            print(header)
            for matchs in round["matchs"]:
                colors = ["blancs", "noirs"]
                player1_chess_piece_color = random.choice(colors)
                colors.remove(player1_chess_piece_color)
                player2_chess_piece_color = colors[0]
                player1 = matchs[0]
                player2 = matchs[1]
                row = tp.row(
                    [
                        round["matchs"].index(matchs) + 1,
                        f'{player1["lastname"]} {player1["firstname"][0:3]}.',
                        player1_chess_piece_color,
                        "vs",
                        f'{player2["lastname"]} {player2["firstname"][0:3]}.',
                        player2_chess_piece_color,
                        player1["score"],
                        player2["score"],
                    ],
                    15,
                )
                print(row)
            print(bottom)

    def is_round_finish(self, round):
        return True if round["end_date"] != "" else False

    def is_tournament_finish(self, tournament):
        return True if tournament.end_date != "" else False

    def success_creation_tournament(self):
        print("Le tournoi a été crée avec succès ! ")

    def failed_creation_tournament(self):
        print("La création du tournoi a échoué ! ")

    def ask_name_tournament(self):
        name = input("Entrer le nom du tournoi : ")

        return name if f.information_is_ok(name) else self.ask_name_tournament()

    def ask_location_tournament(self):
        location = input("Entrer le lieu du tournoi : ")

        return (
            location
            if f.information_is_ok(location)
            else self.ask_location_tournament()
        )

    def ask_description_tournament(self):
        description = input("Entrer la description du tournoi : ")

        return (
            description
            if f.information_is_ok(description)
            else self.ask_description_tournament()
        )

    def ask_nb_turns(self):
        nb_turns = input("Entrer le nombre de tours du tournoi : ")

        return nb_turns if f.nb_turn_is_ok(nb_turns) else self.ask_nb_turns()

    def ask_update_tournament(self):
        update = input("Merci d'entrer le nouveau nom du tournoi : ")

        return update if f.information_is_ok(update) else self.ask_update_tournament()

    def ask_results(self, matchs_list):
        nb_match = 1
        list_player_cumulate_points = []
        while nb_match <= len(matchs_list):
            player = matchs_list[int(nb_match) - 1]
            player1 = player[0]
            player2 = player[1]
            player1_id = player1[0]
            player2_id = player2[0]
            print(
                f"Vous allez entrer les résultats du match n°{nb_match} :\
                        {player1_id} VS\
                        {player2_id}"
            )

            for index, value in enumerate(player):
                score = input(f"Entrez le score du joueur {player[index][0]} : ")
                player[index][1] = float(score)
                dict_player_point = {}
                dict_player_point["id"] = player[index][0]
                dict_player_point["cumulate_score"] = float(score)
                list_player_cumulate_points.append(dict_player_point)
            nb_match += 1

        return matchs_list, list_player_cumulate_points

    def tournament_is_over(self, winner):
        print("Le tournoi est fini ! ")
        print(
            f'le vainqueur du tournoi est le joueur : {winner["id"]} avec un score final de {winner["cumulate_score"]}'
        )

    def forbidden_modify_tournament(self, tournament):
        print(
            f'Le tournoi "{tournament.name}" est terminé. Vous ne pouvez plus entrer de résulats.'
        )

    def display_not_tournament_in_db(self):
        print("Il n'y a aucun tournoi en base de donnée !")

    def display_tournament_results(self, results):
        header = tp.header(["Id joueur", "Score", "Classement"], 15)
        print(header)
        for index, player in enumerate(results):
            print(tp.row([player["id"], player["cumulate_score"], index + 1], 15))
        print(tp.bottom(3, 15))

    def display_players_to_add(self, list_players: list) -> list:
        # tableau
        header = tp.header(["Numéro du joueur", "Prénom", "Nom"], 20)
        print(header)
        for index, player in enumerate(list_players):
            row = tp.row([index + 1, player.firstname, player.lastname], 20)
            print(row)
        print(tp.bottom(3, 20))

        user_choice = input(
            "Séléctionné le joueur a enregistrer : \nappuyez sur [f] pour filtrer\n[b] pour quitter :"
        )

        return user_choice

    def display_all_tournament_players(self, tournament):
        players = tournament.players
        tp.banner(f"Player of {tournament.name} ")
        header = tp.header(
            ["id", "lastname", "firstname", "gender", "birthdate"], width=20
        )
        print(header)
        for player in players:
            list_values = list(player.values())
            row = tp.row(list_values, width=20)
            print(row)

        bottom = tp.bottom(5, width=20)

        print(bottom)

    # Si le choix est in valide
    def invalid_choice(self):
        print("Choix invalide. Veuillez réessayer.")

    def ask_filter(self, list_players):
        new_list_players = []
        name = input("Entrez le nom : ")
        for player in list_players:
            if player.lastname == name:
                new_list_players.append(player)

        if len(new_list_players) == 0:
            print("Vous avez ajouté tous les joueurs.")
            return
        choice_filter = self.display_players_to_add(new_list_players)
        if (
            f.ranking_is_ok(choice_filter)
            and int(choice_filter) <= len(new_list_players)
            and int(choice_filter) > 0
        ):
            new_list_players.pop(int(choice_filter) - 1)
            player_add = list_players.pop(int(choice_filter) - 1)
            player_add_lastname = player_add.lastname
            player_add_firstname = player_add.firstname
            print(f"Vous avez ajouté : {player_add_lastname} {player_add_firstname}")

            return player_add

    def success_player_add_to_tournament(self, player_add: object):
        player_add_lastname = player_add.lastname
        player_add_firstname = player_add.firstname

        print(f"Vous avez ajouté : {player_add_lastname} {player_add_firstname}")
