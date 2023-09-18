import functions as f
import tableprint as tp


class PlayerView:
    """A class representing the view for a class <player>"""

    def display_players_menu(self) -> str:
        """Displays the player management menu

        Returns:
            str: user's choice.

        """
        tp.banner("PLAYERS MENU         ")

        print("1. Create new player")
        print("2. List one player")
        print("3. List all players")
        print("4. Edit existing player")
        print("5. Remove player")

        print("[b] Back to main menu")

        choice = input("Votre choix: ")

        return choice

    def display_all_players(self, players: list) -> None:
        """Displays the list of all players present in the database.

        Arguments:
            list : a list of <player> objects.
        """
        nb_player = len(players)
        print(f"Nombre de joueurs total : {nb_player}")
        headers = tp.header(
            ["Id", "Nom", "Prénom", "Genre", "Né le"], 20, align="center"
        )
        print(headers)
        for player in players:
            print(
                tp.row(
                    [
                        player.id,
                        player.lastname,
                        player.firstname,
                        player.gender,
                        player.birthdate,
                    ],
                    20,
                    align="left",
                )
            )
        print(tp.bottom(5, 20))

    def display_player_view(self, player: object) -> None:
        """Displays a player from the database.

        Arguments:
            player -- object : the player should be displayed
        """
        headers = tp.header(
            ["Id", "Nom", "Prénom", "Genre", "Né le"], 20, align="center"
        )

        row = tp.row(
            [
                player.id,
                player.lastname,
                player.firstname,
                player.gender,
                player.birthdate,
            ],
            20,
            align="left",
        )
        print(headers)
        print(row)
        print(tp.bottom(5, 20))

    def ask_id(self) -> str | None:
        """Asks the user the player's id.

        Returns:
            str: the player's id

        """
        player_id = input("Quel est l'id du joueur? ")

        return player_id if f.id_is_ok(player_id) else self.ask_id()

    def ask_lastname(self) -> str:
        """Asks the player's lastname.

        Returns:
            str: the player's lastname.

        """
        lastname = input("Quel est le nom du joueur? ")

        return lastname if f.information_is_ok(lastname) else self.ask_lastname()

    def ask_firstname(self) -> str:
        """Asks the player's firstname.

        Returns:
            str: the player's firstname.
        """
        firstname = input("Quel est le prénom du joueur? ")

        return firstname if f.information_is_ok(firstname) else self.ask_firstname()

    def ask_gender(self) -> str:
        """Asks the player's gender.

        Returns:
            str: the player's gender.
        """
        gender = input("Quel est votre sexe (masculin ou féminin) ? \n [H/F]")

        return gender if f.gender_is_ok(gender) else self.ask_gender()

    def ask_birth_date(self) -> str:
        """Ask the player's birthdate.

        Returns:
            str: the player's birthdate.
        """
        birth_date = input("Quel est votre date de naissance (format dd-mm-yyyy) ? ")

        return birth_date if f.birth_is_ok(birth_date) else self.ask_birth_date()

    def ask_rank(self) -> str:
        """Asks the player's rank.

        Returns:
            str: the player's rank.
        """
        rank = input("Quel est le rang du joueur ? ")

        return rank if f.ranking_is_ok(rank) else self.ask_rank()

    def ask_add_another_player(self) -> str:
        """Asks the user if they want to add a new player

        Returns:
            str: the user's choice.
        """
        continu = input("Voulez-vous ajouter un autre joueur ? [y/n] ")

        return continu if f.verify_continu(continu) else self.ask_add_another_player()

    def ask_column_update(self) -> str:
        """Asks the user which player data to modify

        Returns:
            str: the user's choice.
        """
        column = input(
            "Quelle colonne souhaitez vous modifier : \n 1. Nom\n 2. Prénom\n 3. Genre\n 4. Birthdate\n "
        )

        return column if f.verify_column_to_update(column) else self.ask_column_update()

    def ask_data(self, column_name: str) -> str:
        """Asks to the user to enter the new player characteristic

        Arguments:
            column_name -- the characteristic to modify

        Returns:
            str : the user's choice
        """
        data = input("Entrer la nouvelle donnée :  ")
        return data if f.verify_data(column_name, data) else self.ask_data(column_name)

    def success_add_player_view(self) -> None:
        """Informs the user that the player was successfully created"""
        print("Le joueur a été ajouté avec succès ! ")

    def success_editing_player_view(self) -> None:
        """Informs the user that the player was successfully edited"""
        print("Le joueur a été modifié avec succès ! ")

    def failed_editing_player_view(self) -> None:
        """Informs the user that the player could not be edited"""
        print(
            "Le joueur n'a pas pu être modifié car il n'existe pas en base de donnée."
        )

    def success_remove_player_view(self) -> None:
        """Informs the user that the player was successfully deleted."""
        print("Le joueur a été supprimé de la base de donnée avec succès  ! ")

    def player_no_exist_view(self) -> None:
        """Informs the user that the requested player does not exist in the database."""
        print("Le joueur n'existe pas en base de donnée ! ")

    def no_existing_players_view(self) -> None:
        """Informs the user that they are no players in the database."""
        print("Il n'y a aucun joueur en base de donnée ! ")

    def player_already_exist_view(self, player: object) -> None:
        """Informs the user that the player already exists in the database.

        Arguments:
            player -- object : a <player> object
        """
        print(
            f"Le joueur : {player.lastname} {player.firstname} existe déjà en base de donnée !"
        )

    def id_already_exist_view(self, id_player: str) -> None:
        """Informs the user that the id is already exists in the database.

        Arguments:
            id_player -- str : the player's id
        """
        print(f"L'id n°{id_player} existe déjà en base de donnée ! ")

    # Si le choix est invalide
    def invalid_choice(self) -> None:
        """Informs the user that his choice is invalid."""
        print("Choix invalide. Veuillez réessayer.")
