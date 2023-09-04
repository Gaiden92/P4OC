def information_is_ok(variable)-> bool:
    variable = variable.strip()

    for caractere in variable:
            if not caractere.isalpha() and not caractere  == " ":
                return False

    return False if not variable else True


def birth_is_ok(variable)-> bool:
    variable = variable.split("-")
    for c in variable:
            if not c.isnumeric() or c.isalpha():
                return False
    return True  


def gender_is_ok(variable)-> bool:
    gender = variable.casefold()

    return False if gender != "h" and gender != "f" else True

def ranking_is_ok(variable)-> bool:
    return False if not variable.isnumeric() else True


def verify_continu(variable)-> bool:
    return False  if variable != "n" and variable != "y" else True   


def verify_column_to_update(variable)-> bool:
            
    return False if not variable.isnumeric() or int(variable) > 5 or int(variable) == 0 else True

def verify_data(column_name:str, data)->bool:
    match column_name:
        case  "1":
            return False if  not information_is_ok(data) else True
        case  "2":
            return False if  not information_is_ok(data) else True

        case "3":
            return False if not gender_is_ok(data) else True
    
        case "4":
            return False if not birth_is_ok(data) else True
    
        case "5":  
            return False if not ranking_is_ok(data) else True

def get_column_name_by_number(number):
    match  number:
        case "1":
            column_name = "lastname"
        case "2":    
            column_name = "firstname"
        case "3":    
            column_name = "gender"
        case "4":    
            column_name = "birthdate"
        case "5":
            column_name = "rank"
        case other_:
            print("")
    return column_name


def is_over(list):
    return True if len(list) == 2 else False

def verify_choice_match_number(choice, list_match):
    return False if not choice.isnumeric() or int(choice) > len(list_match) or  int(choice) < 1 else True 


def already_played_together(rounds:list,players_names_list:list)->bool:
    for round in rounds:
        for match in round["matchs"]:
            print(match)
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