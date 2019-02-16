import random
from bot_base import GardenBotBase

class GardenBot(GardenBotBase):
    def __init__(self, *args):
        GardenBotBase.__init__(self, *args)
        self.role = self.roles["WORM"]

    def do_turn(self):
        return self.directions["STAY"]


