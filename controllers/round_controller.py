from models.round_model import RoundModel
from views.round_view import RoundView


class RoundController:
    def __init__(self, database) -> None:
        self.model = RoundModel(database)
        self.view = RoundView()
        

    



    def get_rounds(self):
        rounds_list = self.model.get_rounds()
        self.view.display_rounds(rounds_list)
