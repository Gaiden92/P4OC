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

    def __init__(
        self,
        id: str,
        lastname: str,
        firstname: str,
        gender: str,
        birthdate: str,
    ) -> None:
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
        """

        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.gender = gender
        self.birthdate = birthdate

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
        }
        return player

