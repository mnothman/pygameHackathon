from settings import * #20
import pygame as pg
import math

class Player: #21
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self): #22
        sin_a = math.sin(self.angle) #25
        cos_a = math.cos(self.angle) 
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time #28
        speed_sin = speed * sin_a #29
        speed_cos = speed * cos_a #29

        keys = pg.key.get_pressed() #30 all the way down
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos #30
  

        self.check_wall_collision(dx,dy)
        #self.x += dx #idk what this does
        #self.y += dy #idk what this does

        if keys[pg.K_LEFT]: #31
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time 
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time 
        self.angle %= math.tau #31

    def check_wall(self, x, y): #36
        return (x, y) not in self.game.map.world_map #36
    
    def check_wall_collision(self, dx, dy): #37
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy #37


    def draw(self): #32
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angle),
                     self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15) #32



    def update(self): #23
        self.movement() #23

    @property #24
    def pos(self):
        return self.x, self.y

    @property #24
    def map_pos(self):
        return int(self.x), int(self.y)