from sprite_object import * #108
from npc import *
from player import * #remove

class ObjectHandler: #108
    def __init__(self, game):
        self.game = game
        self.player = Player(self) #remove
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/' #108
        add_sprite = self.add_sprite #109
        add_npc = self.add_npc


        #sprite map ADD AROUND SPRITES AND WHAT NOT, grid is 18 by 30
        #add_sprite(SpriteObject(game, path=self.static_sprite_path + 'candlebra.png', pos=(1,1))) #109
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '1.png', pos=(18.5,2))) #109     GOOD DONT LOOK OR TAKES EYES  
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '2.png', pos=(19.5,8.5))) #109    good always watches no eyes    
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '3.png', pos=(18.5,14))) #109        good leave me alone
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '4.png', pos=(2.75,22.5))) #109  good trees picture       
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '5.png', pos=(14,14))) #109   good  help me     
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '6.png', pos=(5,30))) #109        cant run
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '7.png', pos=(7,1.5))) #109         GOOD NO NO NO
        add_sprite(SpriteObject(game, path=self.static_sprite_path + '8.png', pos=(18,30))) #109      GOOD   IT FOLLOWS

        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(1.25,1.25), scale=2, shift = -0.15)) #      SMALL TREE GOOD
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(3,3.25), scale=4, shift = -0.30)) #      BIG TREE GOOD

        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(10.5,10), scale=2, shift = -0.15)) #      SMALL TREE GOOD
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(18.5 ,10), scale=2, shift = -0.15)) #      SMALL TREE GOOD
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(2.75,18), scale=2, shift = -0.15)) #      SMALL TREE GOOD

        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(3,20.25), scale=4, shift = -0.30)) #109      BIG TREE GOOD
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(18.5,28.25), scale=4, shift = -0.30)) #109      BIG TREE GOOD
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'tree.png', pos=(8,13), scale=4, shift = -0.30)) #109      BIG TREE


        add_sprite(AnimatedSprite(game)) #109
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(18.5, 5.5))) #WAS 14.5
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(18.5, 7.5))) #14.5
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

