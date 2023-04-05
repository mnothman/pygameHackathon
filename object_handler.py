from sprite_object import * #108
from npc import *

class ObjectHandler: #108
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/' #108
        add_sprite = self.add_sprite #109
        add_npc = self.add_npc


        #sprite map ADD AROUND SPRITES AND WHAT NOT 
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'candlebra.png', pos=(1,1))) #109
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '1.png', pos=(1,1))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '2.png', pos=(2,7))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '3.png', pos=(5,3))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '4.png', pos=(7,4))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '5.png', pos=(14,2))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '6.png', pos=(16,6))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '7.png', pos=(7,1.5))) #109        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '8.png', pos=(4,8))) #109        

        add_sprite(AnimatedSprite(game)) #109
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
    
        #npc map
        add_npc(NPC(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list] #110
        [npc.update() for npc in self.npc_list]

    def add_npc(self,npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite): #109
        self.sprite_list.append(sprite) #109

