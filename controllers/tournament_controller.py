from datetime import datetime
from datetime import date

from models.tournament_model import TournamentModel
from models.tournament_model import Tournament
from models.player_model import PlayerModel
from views.tournament_view import TournamentView
from classes.round import Round
import functions as f


class TournamentController:
    """ "Une classe représentant le controller de la classe <Tournament>.
    Elle fait le lien entre le model et la vue de la classe <Tournament>.

    Attributs
    ----------
    database : str
        La base de donnée à gérer

    """
    def __init__(self, database: str) -> None:
        """Construit tous les attributs nécessaires de la classe.

        Arguments:
            database -- la base de donnée à gérer.
        """
        self.model = TournamentModel(database)
        self.view = TournamentView()
        self.player_model = PlayerModel(database)

    def get_tournaments_menu(self) -> None:
        """Méthode effectuant le contrôle des entrées utilisateurs du menu principal des tournois.
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
        """Méthode effectuant le contrôle des entrées utilisateurs du menu d"un tournoi spécifique.
        """
        if self.not_tournament_in_database():
            self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament()
            tournament = self.model.get_tournament_by_name(name)
            if tournament:
                while True:
                    choice = self.view.display_tournament_menu(tournament)
                    match choice:
                        case "1":
                            self.enter_match_result(tournament)
                        case "2":
                            self.list_results(tournament)
                        case "3":
                            self.list_tournament_by_name(name)
                        case "4":
                            self.update_tournament(name)
                            return
                        case "5":
                            self.model.delete_tournament(name)
                            return
                        case "b":
                            return
                        case _:
                            self.view.invalid_choice()

    def create_tournament(self) -> None:
        """Méthode effectuant le contrôle des entrées utilisateurs pour la création
        d"un tournoi.
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
        for player in self.player_model.get_all_players():
            list_players.append(player)

        # demander à l'utilisateur les joueurs qu'ils souhaitent enregistrer
        list_all_tournament_players = self.view.display_players_to_add(list_players)

        # serialisation de la liste des joueurs
        for player in list_all_tournament_players:
            list_players_serialized.append(player.serialize_player())

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

        if self.model.create_tournament(tournament):
            self.view.success_creation_tournament()
        else:
            self.view.failed_creation_tournament()

    def list_tournaments(self) -> None:
        """Méthode effectuant le contrôle de l'existance des tournois en base de donnée.
        Le controleur appel la vue qui affichera tous les tournois présent est en base de donnée
        ou si aucun tournoi n'est présent, elle appelera la vue concernée.
        """
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            tournaments = self.model.get_tournaments()
            self.view.display_tournaments(tournaments)

    def list_tournament_by_name(self, name: str) -> None:
        """Méthode effectuant le contrôle de l'existance du tournoi passé en argument.
        Le controleur appel la vue spécifique selon si le tournoi est en base de donnée ou si aucun
        tournoi de ce nom n'est présent.

        Arguments:
            name -- le nom du tournoi à afficher

        Valeurs de retour:
            Si le tournoi est en base de donnée :
                la vue affichant les caractéristiques du tournoi.
            Sinon :
                la vue affichant un message indiquant à l'utilisateur que le tournoi
                demandé n'est pas présent en base de donnée.
        """
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            tournament = self.model.get_tournament_by_name(name)
            self.view.display_tournament(tournament)

    def update_tournament(self, name="") -> None:
        """Méthode effectuant le contrôle de l'existance du tournoi passé en argument
        pour effectuer une modification de ce dernier.

        Keyword Arguments:
            name -- le nom du tournoi à modifier (default: {""})
        """
        if self.not_tournament_in_database():
            self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament() if name == "" else name
            update = self.view.ask_update_tournament()

            self.model.update_tournament(update, name)
            

    def delete_tournament(self) -> None:
        """Méthode effectuant le contrôle de l'existance d'un tournoi en base de donnée
        pour effectuer une suppression de ce dernier.
        """
        if self.not_tournament_in_database():
            self.view.display_not_tournament_in_db()
        else:
            name = self.view.ask_name_tournament()
            self.model.delete_tournament(name)

    def enter_match_result(self, tournament: object) -> None:
        """Méthode effectuant le contrôle des entrées utilisateurs pour enregistrer les résultats des matchs
        et générer le prochain tour.

        Arguments:
            tournament -- un objet <tournament>

        Valeurs de retour:
            la vue spécifique selon le cas rencontré.
        """
        if self.not_tournament_in_database():
            return self.view.display_not_tournament_in_db()
        else:
            if tournament.end_date != "":
                self.view.forbidden_modify_tournament(tournament)
            else:
                self.view.display_rounds(tournament.rounds)

                for round in tournament.rounds:
                    if round["end_date"] == "":
                        matchs = round["matchs"]
                        list_match = self.view.ask_results(matchs)
                        round["matchs"] = list_match
                        round["end_date"] = str(date.today())
                        round["end_hour"] = str(
                            datetime.now().time().strftime("%H:%M:%S")
                        )

                if round["name"] == tournament.nb_turn:
                    tournament.end_date = str(date.today())
                    tournament_results = self.get_tournament_results_by_tournament(
                        tournament
                    )
                    tournament_winner = tournament_results[0]
                    self.view.tournament_is_over(tournament_winner)
                    self.model.update_round_tournament(tournament, tournament.name)
                else:
                    # création du prochain round
                    next_round = self.generate_next_round(tournament.rounds)
                    round_serialized = next_round.serialize_round()
                    tournament.rounds.append(round_serialized)
                    tournament.current_round += 1
                    self.model.update_round_tournament(tournament, tournament.name)

    def already_played_together(self, rounds: list, players_names_list: list) -> bool:
        """Méthode vérifiant si des joueurs se sont déjà renconrtrés lors des tours précédents.

        Arguments:
            rounds -- la liste des tours du tournoi
            players_names_list -- la liste des joueurs du tournoi

        Valeurs de retour:
            Vrai si : les 2 joueurs se sont déjà rencontrés
            Faux si : les 2 joueurs ne se sont pas encore rencontrés
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

    def match_pairing(self, rounds: list, list_trier: list) -> list:
        """Méthode effectuant les pairs des matchs.

        Arguments:
            rounds -- la liste des tours du tournoi
            list_trier -- la liste des joueurs trier par score

        Valeurs de retour:
            la liste des matchs du prochain tour.
        """
        index_player1 = 0
        index_player2 = index_player1 + 1
        matchs = []
        while index_player1 < len(list_trier):
            try:
                if self.already_played_together(
                    rounds, [list_trier[index_player1][0], list_trier[index_player2][0]]
                ):
                    index_player2 += 1
            except IndexError:
                break
            else:
                try:
                    matchs.append(
                        [list_trier[index_player1], list_trier[index_player2]]
                    )
                    list_trier.remove(list_trier[index_player2])
                    list_trier.remove(list_trier[index_player1])
                except IndexError:
                    matchs.append([list_trier[0], list_trier[1]])
                    list_trier.remove(list_trier[1])
                    list_trier.remove(list_trier[0])
                index_player2 = index_player1 + 1

        return matchs

    def generate_next_round(self, rounds: list) -> object:
        """Méthode générant le prochain tour.

        Arguments:
            rounds -- la liste des tours précedent du tournoi

        Valeurs de retour:
            le tour suivant sous forme d'un objet <round>
        """
        previous_round = rounds[-1]
        new_round = Round(previous_round["name"] + 1)
        list_players = []
        for match in previous_round["matchs"]:
            for player in match:
                list_player = [player[0], player[1]]
                list_players.append(list_player)

        # trier par score
        liste_trier_par_score = sorted(
            list_players, key=lambda player: float(player[1]), reverse=True
        )

        new_round.matchs = self.match_pairing(rounds, liste_trier_par_score)

        return new_round

    def get_tournament_results_by_tournament(self, tournament:object) -> list:
        """Méthode qui récupère les résultats du dernier tour du tournoi.

        Arguments:
            tournament -- un objet <tournament>

        Valeurs de retour:
            la liste des résultats trier par score.
        """
        last_round = tournament.rounds[-1]
        matchs = last_round["matchs"]
        list_tournament_results = []
        for match in matchs:
            for player_informations in match:
                player_name = player_informations[0]
                player_final_score = player_informations[1]
                list_tournament_results.append(
                    {"name": player_name, "score": player_final_score}
                )
        list_tournament_results_sort = sorted(
            list_tournament_results, key=lambda player: player["score"], reverse=True
        )

        return list_tournament_results_sort

    def not_tournament_in_database(self) -> bool:
        """Méthode vérifiant l'existence d'au moins un tournoi en base de donnée

        Valeurs de retour:
            True si au moins un tournoi existe sinon False 
        """
        return True if self.model.not_tournament_in_database() else False

    def list_results(self, tournament: object) -> None:
        """Méthode appelant la vue d'un tournoi afin d'afficher le résultat de ce dernier.

        Arguments:
            tournament -- un objet <tournament>

        Valeur de retour:
            None
        """
        results = self.get_tournament_results_by_tournament(tournament)
        return self.view.display_tournament_results(results)

    def list_name_and_date(self) -> None:
        """Méthode appelant la vue d'un tournoi afin d'afficher le nom et la date de ce dernier

        Valeurs de retour:
            None
        """
        name = self.view.ask_name_tournament()
        tournament = self.model.get_tournament_by_name(name)
        if tournament:
            return self.view.display_tournament(tournament)
        else:
            self.view.display_not_tournament_in_db()

    def list_round_and_match(self) -> None:
        """Méthode appelant la vue d'un tournoi afin d'afficher ses tours et ses matchs

        Valeurs de retour:
            None
        """
        name = self.view.ask_name_tournament()
        tournament = self.model.get_tournament_by_name(name)
        if tournament:
            return self.view.display_rounds(tournament.rounds)
        else:
            self.view.display_not_tournament_in_db()

    def get_all_tournament_players(self) -> None:
        """Méthode appelant la vue d'un tournoi afin d'afficher tous les joueurs participant 

        Valeurs de retour:
            None
        """
        name = self.view.ask_name_tournament()
        tournament = self.model.get_tournament_by_name(name)

        if tournament:
            players = tournament.players
            sorted_list_players = sorted(players, key=lambda k: k["lastname"])
            tournament.players = sorted_list_players
            return self.view.display_all_tournament_players(tournament)
        else:
            return self.view.display_not_tournament_in_db()
