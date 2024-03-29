from settings import * #20
import pygame as pg
import math

class Player: #21
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()

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

        if keys[pg.K_LEFT]: #31 #82 these 4 were commented
           self.angle -= PLAYER_ROT_SPEED * self.game.delta_time  #82
        if keys[pg.K_RIGHT]: #82
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time  #82
        self.angle %= math.tau #31 keep here dont comment 

    def get_damage(self, damage): #player taking dmg
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over() #call from earlier

    def check_wall(self, x, y): #36
        return (x, y) not in self.game.map.world_map #36
    
    def check_wall_collision(self, dx, dy): #37
        scale = PLAYER_SIZE_SCALE / self.game.delta_time #77
        if self.check_wall(int(self.x + dx * scale), int(self.y)): #77 added * scale
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)): #77 added * scale
            self.y += dy #37

    def check_game_over(self):
        if self.health < 1:
            self.game.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
    
    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def draw(self): #32
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angle),
                     self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15) #32

    def mouse_control(self): #79
        mx, my = pg.mouse.get_pos() #79
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT: #80
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self): #23
        self.movement() #23
        self.mouse_control() #81
        self.recover_health()

    @property #24
    def pos(self):
        return self.x, self.y

    @property #24
    def map_pos(self):
        return int(self.x), int(self.y) #make it to where if your health is below a certain level u do the breathing sound