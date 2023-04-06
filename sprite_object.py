import pygame as pg
from settings import *
import os #100
from collections import deque #100

class SpriteObject:
    def __init__(self, game, path='resources/sprites/slender/1.png', pos=(10.5, 3.5), scale=.5, shift=0.0): #88 #98 added scale used to be 1.0 and shift
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
        

class AnimatedSprite(SpriteObject): #100
    def __init__(self, game, path='resources/sprites/animated_sprites/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0] #101 get path to folder with sprites in them 
        self.images = self.get_images(self.path) #101 load with get images
        self.animation_time_prev = pg.time.get_ticks() #103
        self.animation_trigger = False #103

    def update(self): #106
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images): #105
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0] #105

    def check_animation_time(self): #104
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True #104


    def get_images(self, path): #102, download images then place in queue
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images