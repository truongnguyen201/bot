class GardenBotBase():
    def __init__(self, *args):
        tile_types, directions, valid_moves, teams, roles = args
        self.tile_types = tile_types
        self.directions = directions
        self.valid_moves = valid_moves
        self.game_rule = None
        self.state = None
        self.roles = roles
        self.role = None
        self.teams = teams
        self.my_team = None
        self.x = None
        self.y = None
        self.is_scared = False
        self.is_caught = False
        self.fruit_carrying = 0
        self.map = None
        self.map_width = 0
        self.map_height = 0
        self.allies = None
        self.enemies = None
        self.current_turn = 0

    def preset(self, game_rule, game_state):
        state = game_state["allies"][self.role]
        map_state = game_state["map"]
        self.game_rule = game_rule
        self.map_width = len(map_state)
        self.map_height = len(map_state[0])
        self.my_team = game_state["myTeam"]
        self.chest_x = state["x"]
        self.chest_y = state["y"]

    def update_state(self, game_rule, game_state):
        allies = game_state["allies"]
        self.state = allies[self.role]
        self.x = self.state["x"]
        self.y = self.state["y"]
        self.is_scared = self.state["isScared"]
        self.is_caught = self.state["isCaught"]
        self.fruit_carrying = self.state["fruitCarrying"]
        self.map = game_state["map"]
        self.enemies = game_state["enemies"]
        self.allies = list(filter(lambda a: a != self.state, allies))
        self.current_turn = game_state["turn"]

    def start(self, game_rule, game_state):
        self.preset(game_rule, game_state)
        self.do_start()

    def do_start(self):
        pass

    def turn(self, game_rule, game_state):
        self.update_state(game_rule, game_state)
        return self.do_turn()

    def do_turn(self):
        return None

    def get_name(self):
        return "bot"
