import pygame as pg #38
import math 
from settings import *

class RayCasting: #39
    def __init__(self, game): 
        self.game = game #39
        self.ray_casting_result = [] #65
        self.objects_to_render = [] #65
        self.textures = self.game.object_renderer.wall_textures #65

    def get_objects_to_render(self): #70
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            if proj_height < HEIGHT: #75
                wall_column = self.textures[texture].subsurface( #70
                        offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE #70 was scale instead of 200
                ) #70
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height)) #70
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2) #70
            else: #75
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height #75
                wall_column = self.textures[texture].subsurface( #75
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2, #75
                    SCALE, texture_height #75
                ) 
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT)) #75
                wall_pos = (ray * SCALE, 0) #75 #75

            self.objects_to_render.append((depth, wall_column, wall_pos)) #70

    def ray_cast(self): #40
        self.ray_casting_result = [] #69
        texture_vert, texture_hor = 1, 1 #66 add to avoid error 
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
                    texture_hor = self.game.map.world_map[tile_hor] #66
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
                    texture_vert = self.game.map.world_map[tile_vert] #66
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth #49


            # depth 
            if depth_vert < depth_hor: #67
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor
            
            #51 before textures before 67 REMOVED WITH BELOW DRAW WALLS
            #if depth_vert < depth_hor:
            #    depth = depth_vert
            #else:
            #    depth = depth_hor #51

            #remove fishbowl effect #57
            depth *= math.cos(self.game.player.angle - ray_angle) #57

            #draw for debug THIS IS WHAT SHOWS THE 2D RAYCASTING ANGLES
            #pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
             #           (100 * ox + 100 * depth * cos_a, 100 * oy  + 100 * depth * sin_a), 2)

            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001) #54 CHANGES HEIGHT OF THE WALL

            #draw walls #55 REMOVED AFTER #67 ALONG WITH OLD DEPTH ABOVE
            #color = [255 / (1 + depth ** 5 * 0.00002)] * 3 #56
            #pg.draw.rect(self.game.screen, color, #55
            #             (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)) #55


            # ray casting result #68
            self.ray_casting_result.append((depth, proj_height, texture, offset)) #68


            ray_angle += DELTA_ANGLE #44


    def update(self): #41
        self.ray_cast() #41
        self.get_objects_to_render()