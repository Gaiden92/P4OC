class UserEntry:

    def id_is_ok(self, id_player: str):
        for caractere in id_player:
            if id_player[0:2].isalpha() and id_player[2:].isdigit() and len(id_player) == 6:
                return True
            else:
                return False


    def information_is_ok(self, variable) -> bool:
        variable = variable.strip()

        for caractere in variable:
            if not caractere.isalpha() and not caractere == " ":
                return False

        return False if not variable else True


    def birth_is_ok(self, variable) -> bool:
        variable = variable.split("-")
        for c in variable:
            if not c.isnumeric() or c.isalpha():
                return False
        return True


    def gender_is_ok(self, variable) -> bool:
        gender = variable.casefold()

        return False if gender != "h" and gender != "f" else True


    def ranking_is_ok(self, variable) -> bool:
        return False if not variable.isnumeric() else True


    def verify_continu(self, variable) -> bool:
        return False if variable != "n" and variable != "y" else True


    def verify_column_to_update(self, variable) -> bool:
        if not variable.isnumeric() or int(variable) > 5 or int(variable) == 0:
            return False
        else:
            return True


    def verify_data(self, column_name: str, data) -> bool:
        match column_name:
            case "1":
                return False if not self.information_is_ok(data) else True
            case "2":
                return False if not self.information_is_ok(data) else True

            case "3":
                return False if not self.gender_is_ok(data) else True

            case "4":
                return False if not self.birth_is_ok(data) else True


    def get_column_name_by_number(self, number):
        match number:
            case "1":
                column_name = "lastname"
            case "2":
                column_name = "firstname"
            case "3":
                column_name = "gender"
            case "4":
                column_name = "birthdate"
            case _:
                print("")
        return column_name


    def is_over(self, list):
        return True if len(list) == 2 else False


    def verify_choice_match_number(self, choice, list_match):
        if not choice.isnumeric() or int(choice) > len(list_match) or int(choice) < 1:
            return False
        else:
            return True


    def already_played_together(self, rounds: list, players_names_list: list) -> bool:
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


    def nb_turn_is_ok(self, variable: str) -> bool:
        if not variable or (variable.isnumeric and int(variable) % 2 == 0):
            return True
        else:
            return False
