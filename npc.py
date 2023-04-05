from sprite_object import *
from random import randint, random, choice


class NPC(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/npc/slender/walk.png', pos=(10.5, 5.5), scale=1, shift=0.16, animation_time=.5):
        super().__init__(game, path, pos, scale, shift, animation_time) 
        self.idle_images = self.get_images(self.path + '/idle')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(2, 2) #change this to change the attack distance to melee range
        self.speed = 0.01
        self.size = 10
        self.attack_damage = 8
        self.accuracy = 0.10
        self.alive = True
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        #self.draw_ray_cast()

    def run_logic(self):
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()

            if self.ray_cast_value:
                self.player_search_trigger = True

                if self.dist < self.attack_dist: #only attack when distance to player smaller than atk distance
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()
                    self.game.sound.spooky.play() #add into sounds
                    self.game.object_renderer.static_screen2() #static screen call


            elif self.player_search_trigger:
                self.animate(self.walk_images)
                self.movement()
                #add in sound here the jobro 

            else:
                self.animate(self.idle_images)



    @property #so they cant get hit thru walls, need raycast 
    def map_pos(self):
        return int(self.x), int(self.y)

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy

    def movement(self):
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        next_x, next_y = next_pos
        angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
        dx = math.cos(angle) * self.speed
        dy = math.sin(angle) * self.speed
        self.check_wall_collision(dx, dy)


    def attack(self):
        if self.animation_trigger:
            self.game.sound.npc_shot.play() #make it to where a sound is played when slender hits, ADD TO SOUND FILE
            if random() < self.accuracy:
                self.game.player.get_damage(self.attack_damage) #for player to take damage

    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos: #check if in same tile
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos: #if ray hits wall or npc record, same with vert
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False

    def draw_ray_cast(self):
        pg.draw.circle(self.game.screen, 'red', (100 * self.x, 100 * self.y), 15)
        if self.ray_cast_player_npc():
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y),
                         (100 * self.x, 100 * self.y), 2)