import random
import string


class Player:
    ID = []

    def __init__(self, id, lastname, firstname, gender, birthdate, rank) -> None:
        if id == "":
            self.id = self.generate_id()
        else:
            self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.gender = gender
        self.birthdate = birthdate
        self.rank = rank

        Player.ID.append(self.id)

    def serialize_player(self):
        player = {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "rank": self.rank,
        }
        return player

    def generate_id(self):
        letter = string.ascii_uppercase
        number = string.digits
        letter_str = "".join(random.choice(letter) for _ in range(2))
        number_str = "".join(random.choice(number) for _ in range(4))
        id_player = letter_str + number_str

        return id_player if id_player not in Player.ID else self.generate_id()
