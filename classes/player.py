import random
import string


class Player:
    """Une classe qui représente un joueur.

    Attributs
    ----------
    id : str
        l'id du joueur
    lastname : str
        le nom de famille du joueur
    firstname : str
        le prénom du joueur
    gender : str
        le sexe du joueur
    birthdate : str
        la date de naissance du joueur
    rank : str
        le classement du joueur

    Methodes
    -------
    serialize_player(self):
        Convertit un objet Player en un dictionnaire.
    generate_id(self):
        Génére un id unique pour le joueur.
    """
    ID = []

    def __init__(self, id: str, lastname: str, firstname: str, gender: str, birthdate: str, rank: str) -> None:
        """Construit tous les attributs nécessaire pour l'objet Player.

        Paramètres
        ----------
        id : str
            l'id du joueur
        lastname : str
            le nom de famille du joueur
        firstname : str
            le prénom du joueur
        gender : str
            le sexe du joueur
        birthdate : str
            la date de naissance du joueur
        rank : str
            le classement du joueur
        """
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

    def serialize_player(self) -> dict:
        """Convertit un objet Player en un dictionnaire.

        Retourne:
            Un dictionnaire contenant les information du joueur.
        """
        player = {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "rank": self.rank,
        }
        return player

    def generate_id(self) -> str:
        """Génére un id unique pour le joueur.

        Retourne:
            L'id unique du joueur sous forme d'une chaine de caractère si la condition
            est vrai, sinon la fonction se rappelle.
        """
        letter = string.ascii_uppercase
        number = string.digits
        letter_str = "".join(random.choice(letter) for _ in range(2))
        number_str = "".join(random.choice(number) for _ in range(4))
        id_player = letter_str + number_str

        return id_player if id_player not in Player.ID else self.generate_id()
