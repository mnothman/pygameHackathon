import pygame as pg
from settings import *

class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=(10.5, 3.5), scale=1.0, shift=0.0): #88 #98 added scale and shift
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2 #88
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height() #93
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1 #94
        self.sprite_half_width = 0 #94
        self.SPRITE_SCALE = scale #98
        self.SPRITE_HEIGHT_SHIFT = shift #98

    def get_sprite_projection(self): #92
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE #98
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height)) #scale image to calc position size

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT #99
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift ##98 added height_shift

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos)) #92 #add sprite to array of walls from raycasting

    def get_sprite(self): #89
        dx = self.x - self.player.x #91
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection() #91

    def update(self): #90
        self.get_sprite() #90
        
