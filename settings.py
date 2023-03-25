import math #42

#game settings
RES = WIDTH, HEIGHT = 1600, 900 #1
HALF_WIDTH = WIDTH // 2 #53
HALF_HEIGHT = HEIGHT // 2 #53
FPS = 0 #35

PLAYER_POS = 1.5, 5 #19 mini_map
PLAYER_ANGLE = 0 
PLAYER_SPEED = 0.004 #NEW: make ability to change this when the player picks speed up item
PLAYER_ROT_SPEED = 0.002


FOV = math.pi / 3 #42
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20 #42

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV) #53
SCALE = WIDTH // NUM_RAYS #55