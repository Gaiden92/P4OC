class Player:

    def __init__(self, lastname, firstname, gender, birthdate, rank) -> None:
        self.lastname   = lastname
        self.firstname  = firstname
        self.gender     = gender
        self.birthdate  = birthdate
        self.rank       = rank

    def serialize_player(self):

        player =   {
                        'lastname'  : self.lastname,
                        'firstname' : self.firstname,
                        'gender'    : self.gender,
                        'birthdate' : self.birthdate,
                        'rank'      : self.rank
                    }
        return player