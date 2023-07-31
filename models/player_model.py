from tinydb import TinyDB, Query

class Player:

    def __init__(self, lastname, firstname, gender, birthdate, rank) -> None:
        self.lastname   = lastname
        self.firstname  = firstname
        self.gender     = gender
        self.birthdate  = birthdate
        self.rank       = rank


    def __str__(self) -> str:
        print(f"Nom : {self.lastname}")
        print(f"Prénom : {self.firstname}")
        print(f"Date de naissance : {self.birthdate}")
        print(f"Sexe : {self.gender}")
        print(f"Rang : {self.rank}")





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
        players = self.player_table.all()

        return [ Player( player['lastname'], player['firstname'], player['gender'], player['birthdate'], player['rank'] ) for player in players ]



    def get_player(self, lastname):
        player = self.player_table.get(self.player_query.lastname == lastname)
        if player:
            return Player(player['lastname'], player['firstname'], player['gender'], player['birthdate'], player['rank']) 
        else:
            None    

    def update_player(self, updates, column, lastname, firstname):
        self.player_table.update({column : updates}, (self.player_query.lastname == lastname) and (self.player_query.firstname == firstname))
        print("colonne = ",column, "data = ", updates )

    def delete_player(self, lastname, firstname):
        self.player_table.remove((self.player_query.lastname == lastname) and (self.player_query.firstname == firstname))
        