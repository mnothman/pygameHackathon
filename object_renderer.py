import pygame as pg #59
from settings import * #59


class ObjectRenderer: #60
    def __init__(self, game):
        self.game = game
        self.screen = game.screen #60
        self.wall_textures = self.load_wall_textures() #63

    def draw(self): #73
        self.render_game_objects() #73

    def render_game_objects(self): #72
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos) #72

    @staticmethod #61
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self): #62
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }