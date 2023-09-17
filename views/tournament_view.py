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
                "Tour actuel",
                "Description",
            ],
            width=[25, 20, 15, 15, 12,20],
        )
        bottom = tp.bottom(6, width=[25, 20, 15, 15, 12, 20])
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
            width=[25, 20, 15, 15, 12, 20],
        )
        print(row)
        print(bottom)


    def display_rounds_view(self, rounds: list) -> None:
        for index, round in enumerate(rounds):
            if round["end_date"] == "":
                banner = f"Tour n°{index+1} - en cours     "
            else:
                banner = f"Tour n°{index+1} - terminé      "
            tp.banner(banner)
            header = tp.header(
                [
                    "Match #",
                    "Player 1",
                    "Score P1",
                    "",
                    "Player 2",
                    "Score P2"
                ],
                width=[8, 30, 8, 2, 30,8]
            )
            bottom = tp.bottom(6, width=[8, 30, 8, 2, 30,8])

            print(header)
            for matchs in round["matchs"]:
                player1 = matchs[0]
                player2 = matchs[1]
                row = tp.row(
                    [
                        round["matchs"].index(matchs) + 1,
                        f'{player1["id"]} - {player1["lastname"]} {player1["firstname"][0:3]}.',
                        player1["score"],
                        "vs",
                        f'{player2["id"]} - {player2["lastname"]} {player2["firstname"][0:3]}.',
                        player2["score"]
                    ],
                    width=[8, 30, 8, 2, 30,8]
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
            players = matchs_list[int(nb_match) - 1]

            print(f'Vous allez entrer les résultats du match n°{nb_match} :')

            for index, player in enumerate(players):
                score = input(f'Entrez le score du joueur n°{index+1} : ')
                players[index][1] = float(score)
                dict_player_point = {}
                dict_player_point["id"] = player[0]
                dict_player_point["cumulate_score"] = float(score)
                list_player_cumulate_points.append(dict_player_point)
            nb_match += 1
  
        return matchs_list, list_player_cumulate_points

    def tournament_is_over(self, winner):
        print("Le tournoi est fini ! ")
        print(
            f'le vainqueur du tournoi est le joueur n°{winner["id"]} - {winner["lastname"]} {winner["firstname"]} avec un score final de {winner["cumulate_score"]}'
        )

    def forbidden_modify_tournament(self, tournament):
        print(
            f'Le tournoi "{tournament.name}" est terminé. Vous ne pouvez plus entrer de résulats.'
        )

    def display_not_tournament_in_db(self):
        print("Il n'y a aucun tournoi en base de donnée !")

    def display_tournament_results(self, results):
        header = tp.header(["Joueur", "Score", "Classement"], width=[30, 5, 11])
        print(header)
        for index, player in enumerate(results):
            print(tp.row(   [
                                f'{player["id"]} - {player["lastname"]} {player["firstname"]}',
                                player["cumulate_score"], index + 1
                            ],
                            width=[30, 5, 11]
                        )
                )
        print(tp.bottom(3, width=[30, 5, 11]))

    def display_players_to_add(self, list_players: list) -> object:
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

    # Si le choix est invalide
    def invalid_choice(self):
        print("Choix invalide. Veuillez choisir un joueur valide ou 'b' pour terminer.")

    def success_player_add_to_tournament(self, player_add: object):
        player_add_lastname = player_add.lastname
        player_add_firstname = player_add.firstname

        print(f"Vous avez ajouté : {player_add_lastname} {player_add_firstname}.")

    def user_add_all_players(self):
        print("Vous avez ajouté tous les joueurs.")

    def ask_name_for_filter(self):
        name = input("Entrer un nom : ")
        return name

# colors = ["blancs", "noirs"]
#                 player1_chess_piece_color = random.choice(colors)
#                 colors.remove(player1_chess_piece_color)
#                 player2_chess_piece_color = colors[0]