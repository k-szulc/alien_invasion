class GameStats():

    def __init__(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.get_high_score() #0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):

        try:
            with open('.score') as s:
                high_score = int(s.read())
                return high_score
        except:
            print("No file")
            with open('.score','w') as s:
                s.write('0')
                self.get_high_score()
