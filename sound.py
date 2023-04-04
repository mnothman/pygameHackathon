import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        #for theme self.theme = pg.mixer.load(self.path + 'theme.mp3')
        #pg.mixer.music.set_volume(0.4)
