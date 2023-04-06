import pygame as pg #59
from settings import * #59
from sound import *

class ObjectRenderer: #60
    def __init__(self, game):
        self.game = game
        self.screen = game.screen #60
        self.wall_textures = self.load_wall_textures() #63
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT)) #85
        self.sky_offset = 0 #85
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', RES)
        self.static_screen = self.get_texture('resources/textures/static_screen.png', RES) #implement
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/game_over.png', RES)

    def game_over(self):
        self.screen.blit(self.game_over_image, (0,0))
        self.game.sound.staticlight2.play()#not sure if works or not

    def draw(self): #73
        self.draw_background() #87
        self.render_game_objects() #73
        self.draw_player_health()

    def draw_background(self): #86
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT)) #86

    def draw_player_health(self): #draw health value as string, iterate over and display health
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0,0))

    def static_screen2(self):
        self.screen.blit(self.static_screen, (0,0))

    def render_game_objects(self): #72
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True) #97 #need to sort in tuple so that sprites dont go through walls
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos) #72

    @staticmethod #61
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self): #62
        return {
            1: self.get_texture('resources/textures/peakpx.jpg'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }