import pgzero
import random
from pgzhelper import *

# GAME DIMENSIONS AND MENU
WIDTH = 800
HEIGHT = 600
MENU = 0
GAME = 1
main_state = MENU

# COLORS IN GAME
white = 255, 255, 255
red = 255, 0, 0

# BACKGROUND MUSIC
music_playing = False
#music.play('bgmusic')

# MAIN CHARACTER
mc = Actor('tile_0045.png')
mc.x = 50
mc.y = HEIGHT + 200
mc.scale = 2
mc.images = ['tile_0045.png', 'tile_0046.png']
velocity = 0
gravity = 2.5

# PLATAFORM
platform = [Actor('tile1.png', (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))) for _ in range(7)]

for tile in platform:
    tile.scale = 0.5

# BACKGROUND
bg = Actor('forest.png')
#menubg = Actor('')

# ENEMIES
greenapple = Actor('greenapple.png')
greenapple.x = random.randint(20, 780)
greenapple.y = 0
greenapple.scale = 0.10

redapple = Actor('redapple.png')
redapple.x = random.randint(20, 780)
redapple.y = 0
redapple.scale = 0.040

# LIFE
cherry = Actor('life.png')
cherry.x = random.randint(20, 780)
cherry.y = 0
cherry.scale = 0.10

# SCORE
score = 0
lives = 3
game_over = False
deathsound = False

def update():
    global game_over
    global velocity
    global score
    global lives
    global music_playing

    if main_state == GAME: 
        mc.animate()
        mc.scale = 2
        if main_state == MENU and not music_playing:
            music.play('bgmusic.mp3')
            music_playing = True
        
        # MC MOVES
        if keyboard.left:
            mc.x = mc.x - 5
        if keyboard.right:
            mc.x = mc.x + 5
        
        # MC JUMP
        if keyboard.up:
            velocity = -18
        mc.y = mc.y + velocity
        velocity = velocity + gravity
        
        # MC SCREEN BLOCK 
        if mc.x < 60:
            mc.x = 60
        if mc.x > 740:
            mc.x = 740 
        
        # STOP MC FROM FALLING
        if mc.y > 480: 
            velocity = 0
            mc.y = 470
        if keyboard.down:
            mc.y += 5

        # CHERRY -> + LIFE
        cherry.y += 4
        if cherry.y > 600 or cherry.colliderect(mc):
            cherry.x = random.randint(20, 780)
            cherry.y = 0 
            cherry.scale = 0.10 
        if cherry.colliderect(mc):
            lives = lives + 1
        '''if cherry.y > 600:
            cherry.x = random.randint(20, 780)
            cherry.y = 0 
            cherry.scale = 0.10       
        if cherry.colliderect(mc):
            cherry.x = random.randint(20, 780)
            cherry.y = 0
            cherry.scale = 0.10
            lives = lives + 1
            # sounds.coin.play()'''

        # GOOD RED APPLE -> + POINTS
        redapple.y += 4
        if redapple.y > 600 or redapple.colliderect(mc):
            redapple.x = random.randint(20, 780)
            redapple.y = 0 
            redapple.scale = 0.10 
        if redapple.colliderect(mc):
            lives = lives + 1
        '''if redapple.y > 600:
            redapple.x = random.randint(20, 780)
            redapple.y = 0
            redapple.scale = 0.040
        if redapple.colliderect(mc):
            redapple.x = random.randint(20, 780)
            redapple.y = 0
            redapple.scale = 0.040
            score = score + 1'''

        # GREEN BAD APPLE > - POINTS
        greenapple.y += 4
        if greenapple.y > 600 or greenapple.colliderect(mc):
            greenapple.x = random.randint(20, 780)
            greenapple.y = 0 
            greenapple.scale = 0.10 
        if greenapple.colliderect(mc):
            lives = lives + 1
        '''if greenapple.y > 600:
            greenapple.x = random.randint(20, 780)
            greenapple.y = 0
            greenapple.scale = 0.10
        if greenapple.colliderect(mc):
            greenapple.x = random.randint(20, 780)
            greenapple.y = 0
            greenapple.scale = 0.10
            lives = lives - 1'''
        # GAME OVER IF RUN OUT OF LIVES 
        if lives == 0:
            game_over = True

def on_key_down(key):
    global main_state
    if main_state == MENU and key == keys.SPACE:
        main_state = GAME

def draw():
    screen.clear()
    
    # MENU
    if main_state == MENU:
        screen.draw.text('TESTE', ((WIDTH/2)-70, (HEIGHT/2)-70), color=(white), fontname='public_pixel.ttf', fontsize=30)
        screen.draw.text('PRESS SPACE TO START THE GAME!', (150, 450), color=(white), fontname='public_pixel.ttf', fontsize=15)
    
    # GAME
    elif main_state == GAME:
        bg.draw()
        mc.draw()
        greenapple.draw()
        redapple.draw()
        cherry.draw()
        for p in platform:
            p.draw()
        screen.draw.text('Score: ' + str(score), (10, 15), color=(white), fontname='public_pixel.ttf', fontsize=15)
        screen.draw.text('Lives: ' + str(score), (650, 15), color=(white), fontname='public_pixel.ttf', fontsize=15)
        if game_over:
            screen.draw.text('GAME OVER', ((WIDTH/2)-70, (HEIGHT/2)-70), color=(white), fontname='public_pixel.ttf', fontsize=50)
            screen.draw.text('NICE TRY! SHOULD YOU TRY AGAIN?', (150, 450), color=(white), fontname='public_pixel.ttf', fontsize=20)
            screen.draw.text('FINAL SCORE: ' + str(score), ((WIDTH/2)-70, (HEIGHT/2)-70), color=(red), fontname='public_pixel.ttf', fontsize=15)



''' arrumar a sprite mc
musica
TAMANHO DA SPRITE



'''
