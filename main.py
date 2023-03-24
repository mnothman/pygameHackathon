import pygame as pg #2
import sys
from settings import *
from map import *
from player import * #33

#3
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1 #26
        self.new_game() #17


    def new_game(self): #4
        self.map = Map(self) #16
        self.player = Player(self) #34


    def update(self): #5
        self.player.update() #34
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}') #update screen and show fps in window caption

    def draw(self): #6
        self.screen.fill('black')
        self.map.draw() #18
        self.player.draw() #34

    def check_events(self): #8 if X or esc is pressed
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self): #7
        while True:
            self.check_events() #9
            self.update()
            self.draw()

if __name__ == '__main__': #10
    game = Game()
    game.run()