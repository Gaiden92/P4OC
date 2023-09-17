class Player:
    """A class that represents a player.

    Attributes
    ----------
    id: str
        player id
    lastname: str
        the player's last name
    firstname: str
        the player's first name
    gender: str
        the gender of the player
    birthdate: str
        the player's date of birth
    rank: str
        player ranking

    Methods
    -------
    serialize_player(self):
        Converts a Player object to a dictionary.
    generate_id(self):
        Generates a unique id for the player.
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
        """Constructs all necessary attributes for the Player object.

        Arguments:
            id -- player id
            lastname -- the player's last name
            firstname -- the player's first name
            gender -- the gender of the player
            birthdate -- the player's date of birth
        """

        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.gender = gender
        self.birthdate = birthdate

        # List contenant tous les id des joueurs
        Player.ID.append(self.id)

    def serialize_player(self) -> dict:
        """Converts a Player object to a dictionary.

        Returns:
            A dictionary containing player information.
        """
        player = {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "gender": self.gender,
            "birthdate": self.birthdate,
        }
        return player
