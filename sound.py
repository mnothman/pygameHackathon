import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav') #WHEN WE GET HIT
        self.player_pain.set_volume(0.01)

        self.npc_attack2 = pg.mixer.Sound(self.path + 'npc_attack.wav') #WHEN SLENDER ATTACKS was 
        self.npc_attack2.set_volume(0.02)

        self.spooky = pg.mixer.Sound(self.path + 'spooky.wav')
        self.spooky.set_volume(0.01)

        self.staticlight2 = pg.mixer.Sound(self.path + 'staticlight.wav')
        self.staticlight2.set_volume(0.01)

        #self.spooky = pg.mixer.Sound(self.path + 'spooky.wav')
        #self.spooky.set_volume(0.01)

        #for theme self.theme = pg.mixer.load(self.path + 'theme.mp3')
        #pg.mixer.music.set_volume(0.4)
