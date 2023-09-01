from tinydb import TinyDB, Query

class Player:

    def __init__(self, lastname, firstname, gender, birthdate, rank) -> None:
        self.lastname   = lastname
        self.firstname  = firstname
        self.gender     = gender
        self.birthdate  = birthdate
        self.rank       = rank


    def __str__(self) -> str:
        return  f"{self.lastname} | {self.firstname} | {self.birthdate} | {self.gender} | {self.rank} |"

        # f'Nom : {self.lastname}\n'\
        #         f'Prénom : {self.firstname}\n'\
        #         f'Date de naissance : {self.birthdate}\n'\
        #         f'Sexe : {self.gender}\n'\
        #         f'Classement : {self.rank}\n'



class PlayerModel:
    def __init__(self, database) -> None:
        self.db             = TinyDB(database, indent=4, separators=(',', ': '))
        self.player_table   = self.db.table("players")
        self.player_query   = Query()


    def create_player(self, player):
        self.player_table.insert(   
                                    {
                                        'lastname'  : player.lastname,
                                        'firstname' : player.firstname,
                                        'gender'    : player.gender,
                                        'birthdate' : player.birthdate,
                                        'rank'      : player.rank
                                    }   
                                )


    def get_all_players(self):
        all_players = self.player_table.all()
        
        all_players_list = [ Player( player['lastname'], player['firstname'], player['gender'], player['birthdate'], player['rank'] ) for player in all_players ]
        
        return all_players_list


    def get_player(self, lastname):
        player = self.player_table.get(self.player_query.lastname == lastname)
        if player:
            return Player(player['lastname'], player['firstname'], player['gender'], player['birthdate'], player['rank']) 
        else:
            return None    

    def update_player(self, updates, column, lastname, firstname):
        if self.player_table.update({column : updates}, (self.player_query.lastname == lastname) and (self.player_query.firstname == firstname)):
            return True
        else:
            return False
        

    def delete_player(self, lastname, firstname):
        if self.player_table.remove((self.player_query.lastname == lastname) and (self.player_query.firstname == firstname)):
            return True
        else:
            False
        