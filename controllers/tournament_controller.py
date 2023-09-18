from datetime import datetime
from datetime import date
import copy

from dao.tournament_dao import TournamentDao
from models.tournament import Tournament
from models.match import Match
from dao.player_dao import PlayerDao

from views.tournament_view import TournamentView
from models.round import Round
import functions as f


class TournamentController:
    """A class representing the controller of the <Tournament> class.

    """
    def __init__(self, database: str) -> None:
        """Constructs all necessary attributes of the class.

        Arguments:
            database -- database -- the database to manage.
        """
        self.dao = TournamentDao(database)
        self.view = TournamentView()
        self.player_dao = PlayerDao(database)

    def get_tournaments_menu(self) -> None:
        """Method for controlling user input from the tournament main menu.
        """
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
                case _:
                    self.view.invalid_choice()

    def get_tournament_menu(self) -> None:
        """Method for controlling user entries in the menu of a specific tournament.
        """
        if self.none_tournament_register():
            self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament()
            tournament = self.dao.get_tournament_by_name(name)
            if tournament:
                while True:
                    choice = self.view.display_tournament_menu(tournament)
                    match choice:
                        case "1":
                            self.enter_match_result(tournament)
                        case "2":
                            self.display_results(tournament)
                        case "3":
                            self.list_tournament_by_name(name)
                        case "4":
                            self.update_tournament(name)
                            return
                        case "5":
                            self.dao.delete_tournament(name)
                            return
                        case "6":
                            self.display_rounds(tournament)
                        case "b":
                            return
                        case _:
                            self.view.invalid_choice()

    def create_tournament(self) -> None:
        """Method for creating a tournament

        Returns:
            None
        """
        
        # vérification des entrées de l'utilisateur
        name = self.view.ask_name_tournament()
        if not f.information_is_ok(name):
            return self.view.ask_name_tournament()

        location = self.view.ask_location_tournament()
        if not f.information_is_ok(location):
            return self.view.ask_location_tournament()

        description = self.view.ask_description_tournament()
        if not f.information_is_ok(description):
            return self.view.ask_description_tournament()

        nb_turns = self.view.ask_nb_turns()
        if not f.nb_turn_is_ok(nb_turns):
            return self.view.ask_nb_turns()

        list_players = []
        list_players_serialized = []
        # ajout des joueurs au tournoi
        for player in self.player_dao.get_all_players():
            list_players.append(player)

        # demander à l'utilisateur les joueurs qu'ils souhaitent enregistrer
        list_all_tournament_players = self.add_players_to_tournament(list_players)

        # sérialisation de la liste des joueurs du tournoi
        for player in list_all_tournament_players:
            list_players_serialized.append({"id": player.id, "cumulate_score": 0})

        # création du 1er round
        rounds_list = []
        rounds = Round(1)
        rounds.matchs = rounds.generate_first_round(list_all_tournament_players)
        rounds_serialize = rounds.serialize_round()
        rounds_list.append(rounds_serialize)

        # création de l'objet <Tournoi> pour sauvegarde en base de donnée
        tournament = Tournament(
            name, location, rounds_list, list_players_serialized, description, nb_turns
        )

        # renvoie de la vue approprié de la création du tournoi
        if self.dao.create_tournament(tournament):
            self.view.success_creation_tournament()
        else:
            self.view.failed_creation_tournament()

    def list_tournaments(self) -> None:
        """Method for checking the existence of at least one tournament in the database.
        The controller calls the view which will display all the tournaments present in the database
        or if no tournament is present, it will call the concerned view

        Returns:
            None
        """
        if self.none_tournament_register():
            return self.view.display_not_tournament_in_db()
        else:
            tournaments = self.dao.get_tournaments()
            self.view.display_tournaments(tournaments)

    def list_tournament_by_name(self, name: str) -> None:
        """Method checking the existence of the tournament passed as an argument.
        The controller calls the specific view depending on whether the tournament is in a database or if none
        tournament of this name is not present.

        Arguments:
            name -- the name of the tournament to display

        Returns:
            None
        """
        if self.none_tournament_register():
            return self.view.display_not_tournament_in_db()
        else:
            tournament = self.dao.get_tournament_by_name(name)
            self.view.display_tournament(tournament)

    def update_tournament(self, name="") -> None:
        """Method checking the existence of the tournament passed as an argument
        to make a modification of the latter.

        Keyword Arguments:
            name -- the name of the tournament to modify (default: {""})
        """
        if self.none_tournament_register():
            self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament() if name == "" else name
            update = self.view.ask_update_tournament()

            self.dao.update_tournament(update, name)

    def delete_tournament(self) -> None:
        """Method for checking the existence of a tournament in the database
        to delete it.
        """
        if self.none_tournament_register():
            self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament()
            self.dao.delete_tournament(name)

    def enter_match_result(self, tournament: object) -> None:
        """Method for controlling user input to record match results
        and generate the next round.

        Arguments:
            tournament -- a <tournament> object

        Returns:
            an specific view
        """
        # vérification de la présence d'un tournoi
        if self.none_tournament_register():
            return self.view.display_not_tournament_in_db()
        else:
            # vérification si le tournoi est déjà terminé
            if tournament.end_date != "":
                self.view.forbidden_modify_tournament(tournament)
            else:
                rounds_for_display = self.transform_rounds_for_display(tournament)
                self.view.display_rounds_view(rounds_for_display)
                
                for round in tournament.rounds:
                    if round["end_date"] == "":
                        matchs = round["matchs"]
                        list_match, list_player_cumulate_points = self.view.ask_results(matchs)

                        round["matchs"] = list_match
                        round["end_date"] = str(date.today())
                        round["end_hour"] = str(
                            datetime.now().time().strftime("%H:%M:%S")
                        )
                # vérification s'ils s'agit du dernier tour
                if round["name"] == tournament.nb_turn:
                    tournament.end_date = str(date.today())
                    tournament_results = self.transform_results_for_display(tournament)
                    tournament_winner = tournament_results[0]
                    self.view.tournament_is_over(tournament_winner)
                    self.dao.update_round_tournament(tournament, tournament.name)

                else:
                    # mise à jour des score accumulés des joueurs du tournoi
                    players = tournament.players
                    for player in players:
                        for dict_players in list_player_cumulate_points:
                            if player["id"] == dict_players["id"]:
                                player["cumulate_score"] += dict_players[
                                    "cumulate_score"
                                ]
                    self.dao.update_players_tournament(players, tournament.name)

                    # création du prochain tour
                    next_round = self.generate_next_round(tournament)
                    next_round_serialize = next_round.serialize_round()
                    tournament.rounds.append(next_round_serialize)
                    tournament.current_round += 1
                    self.dao.update_round_tournament(tournament, tournament.name)

    def already_played_together(self, rounds: list, players_names_list: list) -> bool:
        """Method checking if players have already met in previous rounds.
        Arguments:
            rounds -- 
            players_names_list -- 
        Return values:
            

        Arguments:
            rounds -- the list of tournament rounds
            players_names_list -- the list of tournament players

        Returns:
            True if: the 2 players have already match each others
            False if: the 2 players have not yet match each others
        """
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

    def match_pairing(self, rounds: list, sorted_list: list) -> list:
        """Method performing even matches.

        Arguments:
            rounds -- the list of tournament rounds
            sorted_list -- the list of players sorted by score

        Returns:
            the list of matches for the next round
        """
        index_player1 = 0
        index_player2 = index_player1 + 1
        matchs = []
        while index_player1 < len(sorted_list):
            try:
                if self.already_played_together(
                    rounds,
                    [sorted_list[index_player1][0], sorted_list[index_player2][0]],
                ):
                    index_player2 += 1
            except IndexError:
                break
            else:
                try:
                    sorted_list[index_player1][1] = 0
                    sorted_list[index_player2][1] = 0
                    matchs.append(
                        [sorted_list[index_player1], sorted_list[index_player2]]
                    )
                    sorted_list.remove(sorted_list[index_player2])
                    sorted_list.remove(sorted_list[index_player1])
                except IndexError:
                    sorted_list[0][1] = 0
                    sorted_list[1][1] = 0
                    matchs.append([sorted_list[0], sorted_list[1]])
                    sorted_list.remove(sorted_list[1])
                    sorted_list.remove(sorted_list[0])
                index_player2 = index_player1 + 1

        return matchs

    def generate_next_round(self, tournament: object) -> object:
        """Method generating the next round.

        Arguments:
            tournament -- the <tournament> object

        Returns:
            the next round as a <round> object
        """
        list_rounds = tournament.rounds
        last_round = list_rounds[-1]
        next_round = Round(last_round["name"] + 1)
        list_players = tournament.players

        # trier par score
        list_of_dicts_of_players = sorted(
            list_players, key=lambda player: player["cumulate_score"], reverse=True
        )

        # création d'une liste contenant les ids des joueurs et leur scores
        list_of_lists_of_players = []
        for dicts in list_of_dicts_of_players:
            list_of_lists_of_players.append([dicts["id"], dicts["cumulate_score"]])

        next_round.matchs = self.match_pairing(
            tournament.rounds, list_of_lists_of_players
        )

        return next_round

    def get_tournament_results_by_tournament(self, tournament: object) -> list:
        """Method that retrieves the results of the last round of the tournament.

        Arguments:
            tournament -- a <tournament> object

        Returns:
            the list of results sort by score.
        """
        list_of_players_and_results = tournament.players
        list_tournament_results_sort = sorted(
            list_of_players_and_results,
            key=lambda player: player["cumulate_score"],
            reverse=True,
        )

        return list_tournament_results_sort

    def none_tournament_register(self) -> bool:
        """Method checking the existence of at least one tournament in the database

        Returns:
            True if at least one tournament exists otherwise False
        """
        return True if self.dao.none_tournament_register() else False

    def list_round_and_match(self) -> None:
        """Method calling a tournament view to display its rounds and matches

        Returns:
            None
        """
        name = self.view.ask_name_tournament()
        tournament = self.dao.get_tournament_by_name(name)
        if tournament:
            return self.display_rounds(tournament)
        else:
            self.view.display_not_tournament_in_db()

    def get_all_tournament_players(self) -> None:
        """Method calling a tournament view to display all participating players

        Returns:
            None
        """
        name = self.view.ask_name_tournament()
        tournament = self.dao.get_tournament_by_name(name)

        if tournament:
            list_object_players = [
                self.player_dao.get_player_by_id(player["id"])
                for player in tournament.players
            ]
            list_dict_players = [
                player.serialize_player() for player in list_object_players
            ]
            sorted_list_players = sorted(list_dict_players, key=lambda k: k["lastname"])
            tournament.players = sorted_list_players
            return self.view.display_all_tournament_players(tournament)
        else:
            return self.view.display_not_tournament_in_db()

    def transform_rounds_for_display(self, tournament: object) -> list:
        """Method transforming rounds for diplay

        Arguments:
            tournament -- a tournament object

        Returns:
            list : a list of rounds 
        """
        rounds = tournament.rounds
        new_rounds = copy.deepcopy(rounds)

        for round in new_rounds:
            new_matchs = []
            for match in round["matchs"]:
                player1 = match[0]
                player2 = match[1]
                match_object = Match(player1, player2)

                player1_object = self.player_dao.get_player_by_id(match_object.player1_id)
                player2_object = self.player_dao.get_player_by_id(match_object.player2_id)
                dict_match = [
                                {
                                    "id": player1_object.id,
                                    "lastname": player1_object.lastname,
                                    "firstname": player1_object.firstname,
                                    "score": match_object.player1_score
                                },
                                {
                                    "id": player2_object.id,
                                    "lastname": player2_object.lastname,
                                    "firstname": player2_object.firstname,
                                    "score": match_object.player2_score
                                }
                            ]

                new_matchs.append(dict_match)

            round["matchs"] = new_matchs

        return new_rounds
    
    def display_rounds(self, tournament: object) -> None:
        """Method for displaying the rounds of a tournament

        Arguments:
            tournament -- a tournament object
        """
        news_rounds = self.transform_rounds_for_display(tournament)
        self.view.display_rounds_view(news_rounds)

    def add_players_to_tournament(self, list_players: list) -> list | None:
        """Method for adding players for a tournament

        Arguments:
            list_players -- a list of players

        Returns:
            a list of players or None
        """
        list_choices_players = []
        while True:
            if len(list_players) == 0:
                self.view.user_add_all_players()
                return list_choices_players

            choice = self.view.display_players_to_add(list_players)
            if choice == "f":
                # Filtrer les joueurs par nom
                name = self.view.ask_name_for_filter()
                if name:
                    filtered_list_players = [player for player in list_players if player.lastname == name]
                    filtered_choice = self.view.display_players_to_add(filtered_list_players)
                    if filtered_choice.isdigit() and 1 <= int(filtered_choice) <= len(filtered_list_players):
                        player_filtered_to_add = filtered_list_players[int(filtered_choice) - 1]
                        list_players.remove(player_filtered_to_add)
                        self.view.success_player_add_to_tournament(player_filtered_to_add)
                        list_choices_players.append(player_filtered_to_add)
        
            elif choice.isdigit() and 1 <= int(choice) <= len(list_players):
                player_add = list_players[int(choice) - 1]
                list_players.remove(player_add)
                self.view.success_player_add_to_tournament(player_add)
                list_choices_players.append(player_add)

            elif (
                choice == "b"
                and len(list_choices_players) >= 4
                and len(list_choices_players) % 2 == 0
            ):
                return list_choices_players

            else:
                self.view.invalid_choice()

    def transform_results_for_display(self, tournament: object) -> list:
        """Method for generating a list from a tournament object

        Arguments:
            tournament -- a tournament object

        Returns:
            list : sorted by cumulate score result 
        """
        tournament_players = tournament.players
        new_tournament_players = []

        for player in tournament_players:
            player_id = player["id"]
            player_cumulate_score = player["cumulate_score"]
            new_player = self.player_dao.get_player_by_id(player_id)
            dict_player = {
                            "id" : new_player.id,
                            "lastname" : new_player.lastname,
                            "firstname" : new_player.firstname,
                            "cumulate_score" : player_cumulate_score
                            }
             
            new_tournament_players.append(dict_player)
        sorted_new_tournament_players = sorted(new_tournament_players, key= lambda player : player["cumulate_score"], reverse= True)

        return sorted_new_tournament_players

    def display_results(self, tournament: object) -> None:
        """Method for display the tournament result

        Arguments:
            tournament -- a tournament object
        """
        results = self.transform_results_for_display(tournament)
        self.view.display_tournament_results(results)
