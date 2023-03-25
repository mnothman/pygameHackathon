import pygame as pg #38
import math 
from settings import *

class RayCasting: #39
    def __init__(self, game): 
        self.game = game #39

    def ray_cast(self): #40
        ox, oy = self.game.player.pos #45
        x_map, y_map = self.game.player.map_pos #45


        ray_angle = self.game.player.angle - HALF_FOV + 0.0001 #43
        for ray in range(NUM_RAYS): #44
            sin_a = math.sin(ray_angle) #46
            cos_a = math.cos(ray_angle) #46

            #horizontals 
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1) #50

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth #50

            #verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1) #47
            
            depth_vert = (x_vert - ox) / cos_a #47
            y_vert = oy + depth_vert * sin_a #47

            delta_depth = dx / cos_a #47
            dy = delta_depth * sin_a #47

            for i in range(MAX_DEPTH): #48
                tile_vert = int(x_vert), int(y_vert) #49
                if tile_vert in self.game.map.world_map: 
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth #49


            # depth #51
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth= depth_hor #51

            #draw for debug THIS IS WHAT SHOWS THE 2D RAYCASTING ANGLES
            #pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
             #           (100 * ox + 100 * depth * cos_a, 100 * oy  + 100 * depth * sin_a), 2)

            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001) #54

            #draw walls #55
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3 #56
            pg.draw.rect(self.game.screen, color, #55
                         (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)) #55


            ray_angle += DELTA_ANGLE #44




    def update(self): #41
        self.ray_cast() #41