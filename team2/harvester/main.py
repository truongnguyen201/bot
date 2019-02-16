import random
from bot_base import GardenBotBase


class GardenBot(GardenBotBase):
    def __init__(self, *args):
        GardenBotBase.__init__(self, *args)
        self.role = self.roles["HARVESTER"]
    
    def get_name(self):
        return "TRUONG"

    def do_start(self):
        return

    def do_turn(self):
        self.directions["UP"]
        self.directions["DOWN"]
        self.directions["LEFT"]
        self.directions["RIGHT"]
        self.directions["STAY"]


