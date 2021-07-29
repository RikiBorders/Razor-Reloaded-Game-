import pygame
from pygame import mixer
from sprite_sequences import *
from enemy_classes import *

pygame.mixer.init(22100, -16, 2, 64)
pygame.init()

#used to determine if sounds are toggled
SOUNDS_ON = True

WEAPON_CD_TIMER = 500 #half a second till you can fire
WEAPON_READY = True
SHOOTING = False

PROJECTILES = []

#List of all enemies on the level
ENEMY_LIST = []

#Button lists
BUTTONS = []
LEVEL_BUTTONS = []
OPTIONS_BUTTONS = []
STATS_BUTTONS = []

#Level List
LEVELS = {}

SHOWING_STATS = False


class Explosion():
    '''Explosion object'''

    def __init__(self, window, xpos, ypos, sequence):
        '''explosion constructor'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._sequence = sequence
        self._cooldown= 200 # # in which frame will increment
        self._frame = 0
        self._elapsed = False

    def draw(self):
        '''handle drawing of explosion'''
        if self._elapsed == False:
            if self._frame < len(self._sequence) and self._cooldown <= 0:
                self._window.blit(self._sequence[self._frame], (self._xpos, self._ypos) )

                self._frame += 1
                self._cooldown = 150
            else:
                self._window.blit(self._sequence[self._frame], (self._xpos, self._ypos) )
                self._cooldown -= 50 #Reduce the cooldown

        #Cleanup explosions after animation completes
        if self._frame == len(self._sequence):
            self._elapsed = True

    def is_elapsed(self):
        '''Return elapsed state'''
        return self._elapsed

    def move_offscreen(self):
        '''move offscreen'''
        self._xpos, self._ypos = 3000, 3000


class Button():
    '''Class for buttons (240x130)'''

    def __init__(self, window, sprite, type, xpos, ypos, on_screen):
        '''Button constructor'''
        self._window = window
        self._sprite = sprite
        self._type = type
        self._original_xpos = xpos
        self._original_ypos = ypos
        self._xpos = self._original_xpos
        self._ypos = self._original_ypos
        self._onscreen = on_screen
        self._click_sound = mixer.Sound('sounds/sound_effects/button_click.wav')
        if self._onscreen == False: #Move off screen if not displayed at start
            self._xpos = 2000
            self._ypos = 2000

    def draw(self):
        '''Draw the button to the screen'''
        if self._onscreen == True:
            self._window.blit(self._sprite, (self._xpos, self._ypos))
        else:
            pass

    def check_clicked(self, pos):
        '''Check if the button was clicked''' #Check if button clicked
        global SOUNDS_ON #Used in options
        global SHOWING_STATS

        if pos[0] > self._xpos and pos[0] < self._xpos + 500:
            if pos[1] > self._ypos and pos[1] < self._ypos + 350:
                if self._type == 'none':
                    pass

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:
            if pos[1] > self._ypos and pos[1] < self._ypos + 130:
                if self._type == 'sound_toggle':
                    if SOUNDS_ON == True:
                        self._click_sound.play()

                    if SOUNDS_ON == True:
                        pygame.mixer.music.pause()
                        SOUNDS_ON = False
                    elif SOUNDS_ON == False:
                        pygame.mixer.music.unpause()
                        SOUNDS_ON = True

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:
            if pos[1] > self._ypos and pos[1] < self._ypos + 130:
                if self._type == 'options':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for object in OPTIONS_BUTTONS:
                        object.toggle_visibility()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:
            if pos[1] > self._ypos and pos[1] < self._ypos + 130:
                if self._type == 'close':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for object in STATS_BUTTONS:
                        object.toggle_visibility()
                    SHOWING_STATS = False

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:
            if pos[1] > self._ypos and pos[1] < self._ypos + 130:
                if self._type == 'play': #Show level selection
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS:
                        button.toggle_visibility()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:   #Stage 1 button
            if pos[1] > self._ypos and pos[1] < self._ypos + 55:
                if self._type == 'stage1':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS: #Cleanup buttons
                        button.cleanup()
                    LEVELS['level1'].make_active()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:   #Stage 2 button
            if pos[1] > self._ypos and pos[1] < self._ypos + 55:
                if self._type == 'stage2':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS: #Cleanup buttons
                        button.cleanup()
                    LEVELS['level2'].make_active()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:   #Stage 3 button
            if pos[1] > self._ypos and pos[1] < self._ypos + 55:
                if self._type == 'stage3':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS: #Cleanup buttons
                        button.cleanup()
                    LEVELS['level3'].make_active()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:   #Stage 4 button
            if pos[1] > self._ypos and pos[1] < self._ypos + 55:
                if self._type == 'stage4':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS: #Cleanup buttons
                        button.cleanup()
                    LEVELS['level4'].make_active()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:   #Stage 4 button
            if pos[1] > self._ypos and pos[1] < self._ypos + 55:
                if self._type == 'stage5':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS: #Cleanup buttons
                        button.cleanup()
                    LEVELS['level5'].make_active()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:   #Stage 4 button
            if pos[1] > self._ypos and pos[1] < self._ypos + 55:
                if self._type == 'stage6':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    for button in LEVEL_BUTTONS: #Cleanup buttons
                        button.cleanup()
                    LEVELS['level6'].make_active()

        if pos[0] > self._xpos and pos[0] < self._xpos + 240:
            if pos[1] > self._ypos and pos[1] < self._ypos + 130:
                if self._type == 'quit':
                    if SOUNDS_ON == True:
                        self._click_sound.play()
                    pygame.quit()

    def get_position(self):
        '''Return the button's x and y positions'''
        return (self._xpos, self._ypos)

    def get_type(self):
        '''return button's type'''
        return self._type

    def toggle_visibility(self):
        '''toggle on-screen'''
        if self._onscreen == True: #Move off screen if currently displayed
            self._onscreen = False
            self._xpos = 2000
            self._ypos = 2000
        elif self._onscreen == False: #Move on to screen if currently not displayed
            self._xpos = self._original_xpos
            self._ypos = self._original_ypos
            self._onscreen = True

    def cleanup(self):
        '''cleanup all buttons'''
        self._xpos = 2000
        self._ypos = 2000
        self._onscreen = False

    def return_to_screen(self):
        '''return buttons to the screen'''
        self._xpos = self._original_xpos
        self._ypos = self._original_ypos
        self._onscreen = True


class Level():
    '''Class for each game level'''

    def __init__(self, window, level_id, background, foreground, player, end_time):
        '''Level Constructor'''
        self._window = window
        self._id = level_id
        self._background = background
        self._foreground = foreground
        self._player = player
        self._enemy_list = []
        self._active = False
        self._elapsed = False
        self._end_time = end_time
        self.create_enemies()

    def __repr__(self):
        '''List representation'''
        return 'Level {}. Is active?: {}'.format(self._id, self._active)

    def get_end_time(self):
        '''return the level's end time'''
        return self._end_time

    def get_background(self):
        '''Return background and foreground'''
        return (self._background, self._foreground)

    def is_active(self):
        '''Return if the level is active'''
        if self._active == True:
            return True
        elif self._active == False:
            return False

    def make_active(self):
        '''make the level active'''
        #Cleanup menu buttons
        for button in BUTTONS:
            button.cleanup()
        self._active = True

    def make_deactive(self):
        '''make the level not active'''
        #Cleanup menu buttons
        for button in BUTTONS:
            button.cleanup()
        self._active = False

    def create_enemies(self):
        '''Create enemies for each level'''
        #Level 1 setup
        if self._id == 1 and self._active == True:
            self._player.reset_stats()
            #Stop menu music, change to level music
            if SOUNDS_ON == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/level1_music.wav')
                pygame.mixer.music.play(-1)

            asteroid = Asteroid1(self._window, 1300, 350, 'asteroid1', 500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 550, 'asteroid1', 500)
            self._enemy_list.append(asteroid)
            barrel = Barrel1(self._window, 1300, 200, 'exp_barrel1', 1000)
            self._enemy_list.append(barrel)
            barrel = Barrel1(self._window, 1300, 250, 'exp_barrel1', 1000)
            self._enemy_list.append(barrel)
            asteroid = Asteroid2(self._window, 1300, 210, 'asteroid2', 2000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 350, 'asteroid1', 2500)
            self._enemy_list.append(asteroid)
            barrel = Barrel1(self._window, 1300, 500, 'exp_barrel1', 2700)
            self._enemy_list.append(barrel)
            asteroid = Asteroid2(self._window, 1300, 100, 'asteroid2', 4800)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid2(self._window, 1300, 310, 'asteroid2', 6700)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid2(self._window, 1300, 400, 'asteroid2', 9600)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 500, 'fighter1', 10700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 12900)
            self._enemy_list.append(fighter)
            health_pack = HealthPack(self._window, 1300, 300, health_pack_sprite, 12900)
            self._enemy_list.append(health_pack)
            asteroid = Asteroid1(self._window, 1300, 170, 'asteroid1', 13000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid2(self._window, 1300, 500, 'asteroid2', 13600)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 350, 'asteroid1', 14500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 500, 'asteroid1', 14900)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 500, 'asteroid1', 15700)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 400, 'fighter1', 15800)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 80, 'fighter1', 17400)
            self._enemy_list.append(fighter)
            asteroid = Asteroid2(self._window, 1300, 300, 'asteroid2', 18300)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid2(self._window, 1300, 500, 'asteroid2', 20000)
            self._enemy_list.append(asteroid)
            barrel = Barrel1(self._window, 1300, 100, 'exp_barrel1', 20000)
            self._enemy_list.append(barrel)
            barrel = Barrel1(self._window, 1300, 600, 'exp_barrel1', 21000)
            self._enemy_list.append(barrel)
            asteroid = Asteroid2(self._window, 1300, 310, 'asteroid2', 22200)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 500, 'fighter1', 23600)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 24100)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 200, 'fighter1', 26000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 400, 'fighter1', 26000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 550, 'fighter1', 27500)
            self._enemy_list.append(fighter)
            barrel = Barrel1(self._window, 1300, 100, 'exp_barrel1', 28000)
            self._enemy_list.append(barrel)
            asteroid = Asteroid2(self._window, 1300, 400, 'asteroid2', 30000)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 500, 'fighter1', 31000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 32000)
            self._enemy_list.append(fighter)
            asteroid = Asteroid1(self._window, 1300, 170, 'asteroid1', 33000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid2(self._window, 1300, 500, 'asteroid2', 33500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 350, 'asteroid1', 34500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 200, 'asteroid1', 34900)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 500, 'asteroid1', 36000)
            self._enemy_list.append(asteroid)

            #Add the enemies to the active enemy list
            for enemy in self._enemy_list:
                ENEMY_LIST.append(enemy)

        #Level 2 setup
        if self._id == 2 and self._active == True:
            self._player.reset_stats()
            #Stop menu music, change to level music
            if SOUNDS_ON == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/level2_music.wav')
                pygame.mixer.music.play(-1)

            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 500)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 340, 'fighter1', 1200)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 400, 'shielder1', 3200)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 400, 'fighter1', 3700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 5600)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 200, 'fighter1', 7900)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 9000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 200, 'fighter1', 11000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 300, 'fighter1', 13500)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 400, 'fighter1', 13500)
            self._enemy_list.append(fighter)
            asteroid = Asteroid1(self._window, 1300, 300, 'asteroid1', 17500)
            self._enemy_list.append(asteroid)
            shielder = Shielder1(self._window, 1300, 70, 'shielder1', 17000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 70, 'fighter1', 17700)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 370, 'shielder1', 19000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 370, 'fighter1', 19700)
            self._enemy_list.append(fighter)
            asteroid = Asteroid1(self._window, 1300, 300, 'asteroid1', 21500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 400, 'asteroid1', 21500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 100, 'asteroid1', 23500)
            self._enemy_list.append(asteroid)
            shielder = Shielder1(self._window, 1300, 90, 'shielder1', 24000)
            self._enemy_list.append(shielder)
            shielder = Shielder1(self._window, 1300, 170, 'shielder1', 24000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 130, 'fighter1', 24700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 600, 'fighter1', 26000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 400, 'fighter1', 28000)
            self._enemy_list.append(fighter)
            asteroid = Asteroid2(self._window, 1300, 300, 'asteroid2', 30000)
            self._enemy_list.append(asteroid)
            health_pack = HealthPack(self._window, 1300, 300, health_pack_sprite, 31000)
            self._enemy_list.append(health_pack)
            fighter = Fighter1(self._window, 1300, 400, 'fighter1', 33000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 500, 'fighter1', 34000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 300, 'fighter1', 35600)
            self._enemy_list.append(fighter)
            asteroid = Asteroid2(self._window, 1300, 500, 'asteroid2', 39000)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 42000)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 550, 'shielder1', 46000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 140, 'fighter1', 46700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 540, 'fighter1', 46700)
            self._enemy_list.append(fighter)
            asteroid = Asteroid1(self._window, 1300, 300, 'asteroid1', 50000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 380, 'asteroid1', 50000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 420, 'asteroid1', 54000)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 530, 'fighter1', 56000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 630, 'fighter1', 56000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 330, 'fighter1', 56000)
            self._enemy_list.append(fighter)
            asteroid = Asteroid2(self._window, 1300, 500, 'asteroid2', 62000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid2(self._window, 1300, 200, 'asteroid2', 62600)
            self._enemy_list.append(asteroid)
            fighter = Fighter1(self._window, 1300, 540, 'fighter1', 64000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 240, 'fighter1', 66000)
            self._enemy_list.append(fighter)

            #Add the enemies to the active enemy list
            for enemy in self._enemy_list:
                ENEMY_LIST.append(enemy)

        if self._id == 3 and self._active == True:
            self._player.reset_stats()
            #Stop menu music, change to level music
            if SOUNDS_ON == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/level3_music.wav')
                pygame.mixer.music.play(-1)
            #Make a bunch of trackers
            y_cord = 50
            timer = 1000
            for i in range(10):
                tracker = Tracker1(self._window, 1300, y_cord, 'tracker1', timer)
                self._enemy_list.append(tracker)
                y_cord += 55
                timer += 1000

            tracker = Tracker1(self._window, 1300, 200, 'tracker1', 13000)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 100, 'tracker1', 14500)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 500, 'tracker1', 15000)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 100, 'tracker1', 16500)
            self._enemy_list.append(tracker)
            asteroid = Asteroid2(self._window, 1300, 500, 'asteroid2', 17000)
            self._enemy_list.append(asteroid)
            tracker = Tracker1(self._window, 1300, 600, 'tracker1', 18000)
            self._enemy_list.append(tracker)
            asteroid = Asteroid2(self._window, 1300, 200, 'asteroid2', 18500)
            self._enemy_list.append(asteroid)
            tracker = Tracker1(self._window, 1300, 100, 'tracker1', 20000)
            self._enemy_list.append(tracker)
            asteroid = Asteroid1(self._window, 1300, 250, 'asteroid1', 21500)
            self._enemy_list.append(asteroid)

            y_cord = 650
            timer = 23800
            for i in range(4):
                tracker = Tracker1(self._window, 1300, y_cord, 'tracker1', timer)
                self._enemy_list.append(tracker)
                y_cord -= 80
                timer += 1100

            asteroid = Asteroid1(self._window, 1300, 150, 'asteroid1', 29500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 250, 'asteroid1', 31000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 200, 'asteroid1', 32500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 300, 'asteroid1', 34000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 600, 'asteroid1', 37500)
            self._enemy_list.append(asteroid)
            health_pack = HealthPack(self._window, 1300, 600, health_pack_sprite, 38000)
            self._enemy_list.append(health_pack)
            asteroid = Asteroid1(self._window, 1300, 500, 'asteroid1', 39000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 410, 'asteroid1', 41500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 560, 'asteroid1', 43000)
            self._enemy_list.append(asteroid)

            for enemy in self._enemy_list:
                ENEMY_LIST.append(enemy)

        if self._id == 4 and self._active == True:
            self._player.reset_stats()
            #Stop menu music, change to level music
            if SOUNDS_ON == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/level4_music.wav')
                pygame.mixer.music.play(-1)

            tracker = Tracker1(self._window, 1300, 150, 'tracker1', 500)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 220, 'tracker1', 900)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 310, 'tracker1', 2000)
            self._enemy_list.append(tracker)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 2100)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 3000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 340, 'fighter1', 3700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 500, 'fighter1', 5800)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 200, 'fighter1', 6700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 440, 'fighter1', 8500)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 10000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 12000)
            self._enemy_list.append(fighter)
            tracker = Tracker1(self._window, 1300, 430, 'tracker1', 15000)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 510, 'tracker1', 18600)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 340, 'tracker1', 17700)
            self._enemy_list.append(tracker)
            shielder = Shielder1(self._window, 1300, 560, 'shielder1', 20000)
            self._enemy_list.append(shielder)
            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 23000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 100, 'fighter1', 25000)
            self._enemy_list.append(fighter)
            health_pack = HealthPack(self._window, 1300, 300, health_pack_sprite, 27000)
            self._enemy_list.append(health_pack)
            fighter = Fighter1(self._window, 1300, 300, 'fighter1', 29000)
            self._enemy_list.append(fighter)
            tracker = Tracker1(self._window, 1300, 340, 'tracker1', 31700)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 420, 'tracker1', 33400)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 500, 'tracker1', 34400)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 600, 'tracker1', 35600)
            self._enemy_list.append(tracker)
            shielder = Shielder1(self._window, 1300, 560, 'shielder1', 37000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 300, 'fighter1', 38500)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 500, 'fighter1', 38500)
            self._enemy_list.append(fighter)

            for enemy in self._enemy_list:
                ENEMY_LIST.append(enemy)

        if self._id == 5 and self._active == True:
            self._player.reset_stats()
            #Stop menu music, change to level music
            if SOUNDS_ON == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/level3_music.wav')
                pygame.mixer.music.play(-1)

            eye = EvilEye(self._window, 1300, 300, 'evil_eye1', 500)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 400, 'evil_eye1', 1500)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 300, 'evil_eye1', 2500)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 500, 'evil_eye1', 3700)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 200, 'evil_eye1', 5000)
            self._enemy_list.append(eye)
            asteroid = Asteroid1(self._window, 1300, 150, 'asteroid1', 7000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 180, 'asteroid1', 7000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 210, 'asteroid1', 7500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 250, 'asteroid1', 8000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 350, 'asteroid1', 8500)
            self._enemy_list.append(asteroid)
            eye = EvilEye(self._window, 1300, 200, 'evil_eye1', 8600)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 270, 'evil_eye1', 8650)
            self._enemy_list.append(eye)
            asteroid = Asteroid1(self._window, 1300, 450, 'asteroid1', 8700)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 200, 'asteroid1', 9500)
            self._enemy_list.append(asteroid)
            eye = EvilEye(self._window, 1300, 600, 'evil_eye1', 9500)
            self._enemy_list.append(eye)
            asteroid = Asteroid1(self._window, 1300, 300, 'asteroid1', 9500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 100, 'asteroid1', 11100)
            self._enemy_list.append(asteroid)
            eye = EvilEye(self._window, 1300, 150, 'evil_eye1', 11700)
            self._enemy_list.append(eye)
            asteroid = Asteroid1(self._window, 1300, 50, 'asteroid1', 13000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 90, 'asteroid1', 14000)
            self._enemy_list.append(asteroid)
            health_pack = HealthPack(self._window, 1300, 200, health_pack_sprite, 14000)
            self._enemy_list.append(health_pack)
            asteroid = Asteroid1(self._window, 1300, 140, 'asteroid1', 14000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 160, 'asteroid1', 14500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 330, 'asteroid1', 16500)
            self._enemy_list.append(asteroid)
            eye = EvilEye(self._window, 1300, 550, 'evil_eye1', 17000)
            self._enemy_list.append(eye)
            asteroid = Asteroid1(self._window, 1300, 550, 'asteroid1', 17000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 160, 'asteroid1', 17500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 200, 'asteroid1', 18000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 300, 'asteroid1', 18500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 450, 'asteroid1', 19000)
            self._enemy_list.append(asteroid)
            eye = EvilEye(self._window, 1300, 610, 'evil_eye1', 20000)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 210, 'evil_eye1', 21000)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 410, 'evil_eye1', 21800)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 610, 'evil_eye1', 22900)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 610, 'evil_eye1', 23300)
            self._enemy_list.append(eye)
            asteroid = Asteroid1(self._window, 1300, 200, 'asteroid1', 24000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 600, 'asteroid1', 25500)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 350, 'asteroid1', 25000)
            self._enemy_list.append(asteroid)
            eye = EvilEye(self._window, 1300, 410, 'evil_eye1', 26800)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 610, 'evil_eye1', 27900)
            self._enemy_list.append(eye)
            eye = EvilEye(self._window, 1300, 610, 'evil_eye1', 28700)
            self._enemy_list.append(eye)
            tracker = Tracker1(self._window, 1300, 340, 'tracker1', 30000)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 420, 'tracker1', 30000)
            self._enemy_list.append(tracker)
            health_pack = HealthPack(self._window, 1300, 300, health_pack_sprite, 30000)
            self._enemy_list.append(health_pack)
            tracker = Tracker1(self._window, 1300, 500, 'tracker1', 31300)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 600, 'tracker1', 32000)
            self._enemy_list.append(tracker)
            asteroid = Asteroid1(self._window, 1300, 200, 'asteroid1', 33000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 600, 'asteroid1', 34000)
            self._enemy_list.append(asteroid)
            asteroid = Asteroid1(self._window, 1300, 150, 'asteroid1', 35000)
            self._enemy_list.append(asteroid)
            tracker = Tracker1(self._window, 1300, 500, 'tracker1', 36000)
            self._enemy_list.append(tracker)
            tracker = Tracker1(self._window, 1300, 530, 'tracker1', 37000)
            self._enemy_list.append(tracker)

            for enemy in self._enemy_list:
                ENEMY_LIST.append(enemy)

        if self._id == 6 and self._active == True:
            self._player.reset_stats()
            #Stop menu music, change to level music
            if SOUNDS_ON == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/level6_music.wav')
                pygame.mixer.music.play(-1)

            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 500)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 340, 'fighter1', 1200)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 550, 'shielder1', 4000)
            self._enemy_list.append(shielder)
            fighter = Fighter1(self._window, 1300, 540, 'fighter1', 4700)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 240, 'fighter1', 7000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 640, 'fighter1', 8400)
            self._enemy_list.append(fighter)
            battleship = Battleship(self._window, 1300, 500, 'battleship', 10000)
            self._enemy_list.append(battleship)
            battleship = Battleship(self._window, 1300, 100, 'battleship', 10000)
            self._enemy_list.append(battleship)
            fighter = Fighter1(self._window, 1300, 440, 'fighter1', 17000)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 240, 'fighter1', 19500)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 60, 'fighter1', 24500)
            self._enemy_list.append(fighter)
            fighter = Fighter1(self._window, 1300, 600, 'fighter1', 27500)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 34500)
            self._enemy_list.append(shielder)
            health_pack = HealthPack(self._window, 1300, 300, health_pack_sprite, 35000)
            self._enemy_list.append(health_pack)
            fighter = Fighter1(self._window, 1300, 340, 'fighter1', 35200)
            self._enemy_list.append(fighter)
            shielder = Shielder1(self._window, 1300, 150, 'shielder1', 40500)
            self._enemy_list.append(shielder)
            shielder = Shielder1(self._window, 1300, 350, 'shielder1', 40500)
            self._enemy_list.append(shielder)
            shielder = Shielder1(self._window, 1300, 450, 'shielder1', 40500)
            self._enemy_list.append(shielder)

            for enemy in self._enemy_list:
                ENEMY_LIST.append(enemy)

class Projectile():
    '''Projectile objects'''

    def __init__(self, window, position, velocity, type, damage):
        '''Projectile Constructor'''
        self._window = window
        self._xpos = position[0]
        self._ypos = position[1]
        self._velocity = velocity
        self._damage = damage
        self._sprite = type

    def __str__(self):
        '''String method for projectiles'''
        return 'Projectile of type {} at ({}, {})'.format(self._type, self._xpos, self._ypos)

    def __repr__(self):
        '''String method for projectiles'''
        return 'Projectile of type {} at ({}, {})'.format(self._type, self._xpos, self._ypos)

    def get_xpos(self):
        '''return xpos'''
        return self._xpos

    def get_ypos(self):
        '''return ypos'''
        return self._ypos

    def move_offscreen(self):
        '''hide bullet from player's view'''
        self._ypos = 1500

    def get_damage(self):
        '''Return the bullet's damage'''
        return self._damage

    def update(self):
        '''Update the bullets position'''
        if self._xpos <= 1010:
            self._xpos += self._velocity
            self._window.blit(self._sprite, (self._xpos, self._ypos))
        else:
            ROJECTILES.remove(self)


class Player():
    '''Player Object'''

    def __init__(self, window, animation, xpos, ypos, bullet_type):
        '''Constructor for player'''
        self._window = window
        self._animation = animation
        self._xpos = xpos
        self._ypos = ypos
        self._bullet = projectile_dictionary.get(bullet_type)
        self._bullets = []
        self._health = 100
        self._hitbox = (self._xpos, self._ypos, 160, 55)
        self._multiplier = 1 #Score multiplier

        #Stage statistics
        self._kills = 0
        self._score = 0
        self._dist_travelled = 0

        self._frame_counter = 500
        self._active_animation = player_animations[0][0] #fwd animation by default
        self._sequence_index = 0 #active sequence (i.e forward, up, etc.)
        self._frame_index = 0 #which frame in a sequence

    def reset_stats(self):
        '''Reset player stats/health'''
        #Should be used to start rounds
        self._kills = 0
        self._score = 0
        self._dist_travelled = 0
        self._health = 100

    def get_kills(self):
        '''Return kill count'''
        return self._kills

    def damage(self, damage):
        '''handle player damage'''
        self._health -= damage

    def get_xpos(self):
        '''Return player's x position'''
        return self._xpos

    def get_ypos(self):
        '''Return player's y position'''
        return self._ypos

    def get_health(self):
        '''Return health'''
        return self._health

    def get_score(self):
        '''Return score'''
        return self._score

    def get_multiplier(self):
        '''Return score multiplier'''
        return self._multiplier

    def get_distance(self):
        '''Get distance in meters player has travelled'''
        distance = self._dist_travelled * 0.0002645833 #Conversion
        distance = round(distance, 2)
        return distance

    def reset_multiplier(self):
        '''Reset multiplier'''
        self._multiplier = 1

    def add_score(self, amount):
        '''Add to score'''
        self._score += amount * self._multiplier

    def add_kill(self):
        '''add kill to player kill count'''
        self._kills += 1

    def remove_bullet(self, bullet):
        '''Remove the bullet from bullet list'''
        self._bullets.remove(bullet)

    def get_bullets(self):
        '''Return player's bullet list'''
        return self._bullets

    def remove_bullet(self, bullet):
        '''Remove bullet from list'''
        self._bullets.remove(bullet)

    def switch_active_animation(self, new_sequence_index, animation_index):
        '''Switch the active animation sequence'''
        self._active_animation = player_animations[new_sequence_index][animation_index]
        self._sequence_index = new_sequence_index
        self._frame_index = 0

    def update(self, x, y):
        '''Update player position on the screen'''
        self._xpos = x
        self._ypos = y
        self._window.blit(self._animation[self._sequence_index][self._frame_index], (x, y) )
        self._hitbox = (self._xpos, self._ypos, 140, 55) #Update hitbox

        #Update frame counter, and active animation sequence frame
        if self._frame_counter > 0:
            self._frame_counter -= 100 #Higher # = faster switch
        else:
            self._frame_index += 1
            if self._frame_index >= len(self._animation[self._sequence_index]):
                self._frame_index = 0
            self._frame_counter = 400

        #Update distance
        self._dist_travelled += 1

    def change_bullet_type(self, type):
        '''change the player's bullet type'''
        self._bullet = projectile_dictionary.get(type)

    def shoot_main(self):
        '''Fire player's main weapon'''
        #bullet sound
        if SOUNDS_ON == True:
            shoot_sound = mixer.Sound('sounds/sound_effects/player_laser.wav')
            shoot_sound.play()
        #bullet creation
        bullet = Projectile(self._window, (self._xpos + 118, self._ypos + 34), 10, self._bullet, 10)
        PROJECTILES.append(bullet)
        self._bullets.append(bullet)

    def check_collision(self, projectile, explosion_list, ENEMY_LIST, SOUNDS_ON):
        '''check for collisions'''
        #Check for projectile collision
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:
                if projectile not in self._bullets:

                    #Create explosion at impact
                    make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                    #Damage sound
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['fighter_damaged'].play()
                    #Cleanup bullet
                    projectile.move_offscreen()
                    self._health -= projectile.get_damage()
                    self._multiplier = 1

        #Check for enemy collision
        for enemy in ENEMY_LIST:
            if enemy.get_ypos() < self._hitbox[1] + self._hitbox[3] and enemy.get_ypos() > self._hitbox[1]:
                if enemy.get_xpos() > self._hitbox[0] and enemy.get_xpos() < self._hitbox[0] + self._hitbox[2]:
                    make_impact_explosion(self._window, self._xpos + 115, self._ypos + 20, explosion_list)
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['barrel_explosion'].play()
                    self._health -= 10
                    enemy.kill_self()
                    if enemy in ENEMY_LIST:
                        ENEMY_LIST.remove(enemy)

            if enemy.get_ypos()+ 60 < self._hitbox[1] + self._hitbox[3] and enemy.get_ypos() + 60 > self._hitbox[1]:
                if enemy.get_xpos() + 64 > self._hitbox[0] and enemy.get_xpos() + 64 < self._hitbox[0] + self._hitbox[2]:
                    explosion = Explosion(self._window, self._xpos + 50, self._ypos, explosion_sequence)
                    explosion_list.append(explosion)
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['barrel_explosion'].play()
                    self._health -= 10
                    enemy.kill_self()
                    if enemy in ENEMY_LIST:
                        ENEMY_LIST.remove(enemy)

    def add_multiplier(self):
        '''Raise the score multiplier'''
        self._multiplier += 1

    def add_health(self, amount):
        '''Add health'''
        self._health += amount
        if self._health >= 110:
            self._health = 110

    def add_distance(self, amount):
        '''Add to total distance moved'''
        self._dist_travelled += abs(amount)

    def reset_position(self):
        '''Reset the player's current position'''
        self._xpos = 50
        self._ypos = 350


def check_buttons():
    '''Check for button clicks'''
    pos = pygame.mouse.get_pos()
    for button in BUTTONS:
        button.check_clicked(pos)


def update(player, player_x, player_y, window, explosion_list):
    '''Update window objects'''
    #Player updates
    player.update(player_x, player_y)

    #Update draw score
    font = pygame.font.Font('freesansbold.ttf', 32)
    small_font = pygame.font.Font('freesansbold.ttf', 16)
    hud = pygame.image.load('sprites/hud.png').convert_alpha()
    initial_color = (55, 240, 102)

    if player.get_health() <= 70 and player.get_health() > 40:
        initial_color = (200, 200, 0)
    elif player.get_health() > 20 and player.get_health() <= 40:
        initial_color = (255, 165, 0)
    elif player.get_health() <= 20:
        initial_color = (255, 30, 30)

    score = font.render('Score: {}'.format(player.get_score()), True, (255, 255, 255))
    multiplier = small_font.render('Multiplier: x{}'.format(player.get_multiplier()), True, (255, 255, 0))
    health = font.render('Health: {}'.format(player.get_health()), True, (initial_color))

    window.blit(hud, (10, 10) )
    window.blit(health, (20, 20) )
    window.blit(score, (20, 50) )
    window.blit(multiplier, (20, 85) )

    #Projectile updates
    for projectile in PROJECTILES:
        projectile.update()

    for enemy in ENEMY_LIST: #Update enemies and their bullets
        enemy.draw()
        #If enemy shoots, then fire

        if enemy.get_type() == 'fighter' or enemy.get_type() == 'tracker' or enemy.get_type() == 'evil_eye' or enemy.get_type() == 'battleship' or enemy.get_type() == 'drone':
            if enemy.get_spawn_timer() <= 0 and enemy.get_xpos() < 1000:
                enemy.shoot(SOUNDS_ON, PROJECTILES)
            else:
                pass

        #If enemy has not spawned yet, update spawn time
        if enemy.get_spawn_timer() > 0:
            enemy.reduce_spawn_timer()

    #Draw explosions
    for explosion in explosion_list:
        explosion.draw()

    pygame.display.update()

def draw_bg(window, bg, bg_x1, bg_x2):
    '''Draw the background(s)'''
    window.blit(bg, (bg_x1, 0) )
    window.blit(bg, (bg_x2, 0) )


def draw_passing_stars(window, bg, fg_x1, fg_x2):
    '''Draw the foreground passing stars'''
    window.blit(bg, (fg_x1, 0) )
    window.blit(bg, (fg_x2, 0) )


def handle_weapon_cooldown():
    '''Handle weapon cooldown'''
    global WEAPON_READY
    global WEAPON_CD_TIMER

    if WEAPON_READY == False:
        WEAPON_CD_TIMER -= 45 #Higher number is lower cooldown
    else:
        pass
    if WEAPON_CD_TIMER <= 0:
        WEAPON_READY = True
        WEAPON_CD_TIMER = 500
    else:
        pass

def boundary_check(player, explosion_list):
    '''Check for anything hitting window boundaries'''
    #Cleanup projectiles
    for projectile in PROJECTILES:
        if projectile.get_xpos() >= 1000:
            PROJECTILES.remove(projectile)
            #Remove projectile from player bullet list
            if projectile in player.get_bullets():
                player.remove_bullet(projectile)

        elif projectile.get_xpos() <= -20:
            PROJECTILES.remove(projectile)

    #Cleanup Enemies
    for enemy in ENEMY_LIST:
        if enemy.get_xpos() <= -200:
            ENEMY_LIST.remove(enemy)
            enemy.kill_self()
            player.damage(10)
            player.reset_multiplier()


def check_collisions(player, explosion_list, window, SOUNDS_ON):
    '''Check for object collisions'''
    for projectile in PROJECTILES:
        #Check player collision
        player.check_collision(projectile, explosion_list, ENEMY_LIST, SOUNDS_ON)
        #Check if player projectile hit enemy
        if projectile in player.get_bullets():
            for enemy in ENEMY_LIST:

                #Check if health pack, otherwise check for regular collision
                if enemy.get_type() == 'health_pack':
                    enemy.check_grabbed(player, projectile, SOUNDS_ON)
                else:
                    enemy.check_collision(projectile, player, explosion_list, SOUNDS_ON)


    #Check for enemy deaths
    for enemy in ENEMY_LIST:

        if enemy.is_alive() == False:
            if enemy in ENEMY_LIST:
                #Create explosion ,then cleanup enemy
                if enemy.get_type() == 'tracker' or enemy.get_type() == 'barrel':
                    try:
                        explosion = Explosion(window, enemy.get_explosion_cords()[0], enemy.get_explosion_cords()[1], explosion_sequence)
                        explosion_list.append(explosion)
                    except AttributeError:
                        pass

                elif enemy.get_type() == 'asteroid':
                    try:
                        explosion = Explosion(window, enemy.get_explosion_cords()[0], enemy.get_explosion_cords()[1], asteroid_explosion_sequence)
                        explosion_list.append(explosion)
                    except AttributeError:
                        pass

                elif enemy.get_type() == 'asteroid2':
                    try:
                        explosion = Explosion(window, enemy.get_explosion_cords()[0] + 40, enemy.get_explosion_cords()[1] + 40, asteroid_explosion_sequence)
                        explosion_list.append(explosion)
                    except AttributeError:
                        pass

                elif enemy.get_type() == 'fighter' or enemy.get_type() == 'shielder':
                    try:
                        explosion = Explosion(window, enemy.get_explosion_cords()[0] + 10, enemy.get_explosion_cords()[1], explosion_sequence2)
                        explosion_list.append(explosion)
                    except AttributeError:
                        pass

                elif enemy.get_type() == 'evil_eye':
                    try:
                        explosion = Explosion(window, enemy.get_explosion_cords()[0] + 10, enemy.get_explosion_cords()[1], blood_impact_sequence)
                        explosion_list.append(explosion)
                    except AttributeError:
                        pass

                ENEMY_LIST.remove(enemy)


def make_impact_explosion(window, xpos, ypos, explosion_list):
    '''create impact explosion at the given coordinates'''
    #Create an explosion after impact
    explosion = Explosion(window, xpos - 20, ypos, impact_explosion_sequence)
    explosion_list.append(explosion)


def make_eye_impact_explosion(window, xpos, ypos, explosion_list):
    '''create blood impact explosion at the given coordinates'''
    #Create an explosion after impact
    explosion = Explosion(window, xpos - 20, ypos, blood_impact_sequence)
    explosion_list.append(explosion)


def make_shield_impact_explosion(window, xpos, ypos, explosion_list):
    '''create shield impact explosion at the given coordinates'''
    #Create an explosion after impact
    explosion = Explosion(window, xpos - 20, ypos, shield_impact_sequence)
    explosion_list.append(explosion)


def check_stage_selected(player):
    '''Check to see if a level was selected'''
    #If flag is returned false, then the level was selected
    flag = True #True by default
    for level in LEVELS.values():

        if level.is_active() == True:#If a level is active, turn off menu
            flag = False
            return flag

    return flag


def check_level_active():
    '''check for an active level'''
    for level in LEVELS.values():
        if level.is_active() == True:
            level.create_enemies()
            level.make_deactive()
            current_level = level
            return current_level
    return None

def update_background(current_level):
    '''change the current background'''
    bg = current_level.get_background()[0]
    fg = current_level.get_background()[1]
    return (bg, fg)


def get_level_end_timer(current_level):
    '''get the end time for the level'''
    try:
        timer = current_level.get_end_time()
        return timer

    except AttributeError: #Return nothing if no level selected (none type)
        return None


def update_level_timer(timer):
    '''reduce the level timer'''
    timer -= 10
    return timer


def main():
    '''Main function'''
    global WEAPON_READY
    global SHOWING_STATS
    #Window Setup
    window = pygame.display.set_mode( (1000, 700) )
    window.fill( (0, 0, 0) )
    pygame.display.set_caption('Razor Reloaded')
    pygame.display.set_icon(pygame.image.load('sprites/main_menu/icon.png'))

    #Background image setup
    bg = pygame.image.load('sprites/space_background1.png').convert_alpha()
    nebula_bg = pygame.image.load('sprites/nebula_background.png').convert_alpha()
    eclipse_bg = pygame.image.load('sprites/eclipse_bg.png').convert_alpha()
    red_nebula_bg = pygame.image.load('sprites/red_nebula_bg.png').convert_alpha()
    horizon_bg = pygame.image.load('sprites/horizon_bg.png').convert_alpha()
    blue_bg = pygame.image.load('sprites/blue_bg.png').convert_alpha()
    bg_x = 0
    bg_x2 = bg.get_width()
    passing_stars = pygame.image.load('sprites/passing_stars1.png').convert_alpha() #Passing stars should be optional per level
    passing_dust = pygame.image.load('sprites/passing_dust.png').convert_alpha()
    ps_x = 0
    ps_x2 = passing_stars.get_width()

    #Player setup
    player_x = 50
    player_y = 350
    player = Player(window, player_animations, player_x, player_y, 'bullet')
    player_xChange = 0
    player_yChange = 0

    #Create the levels
    Level1 = Level(window, 1, bg, passing_stars, player, 47000)
    LEVELS['level1'] = Level1
    Level2 = Level(window, 2, eclipse_bg, passing_dust, player, 80000)
    LEVELS['level2'] = Level2
    Level3 = Level(window, 3, blue_bg, passing_stars, player, 50000)
    LEVELS['level3'] = Level3
    Level4 = Level(window, 4, nebula_bg, passing_stars, player, 47500)
    LEVELS['level4'] = Level4
    Level5 = Level(window, 5, red_nebula_bg, passing_stars, player, 47000)
    LEVELS['level5'] = Level5
    Level6 = Level(window, 6, horizon_bg, passing_stars, player, 500000)
    LEVELS['level6'] = Level6

    #Create list of explosions
    explosions = []

    #FPS/clock setup
    clock = pygame.time.Clock()
    fps = 60

    #Menu setup
    menu_bg = pygame.image.load('sprites/main_menu/menu_background.png').convert_alpha()
    play_button_sprite = pygame.image.load('sprites/main_menu/play_button.png').convert_alpha()
    play_button = Button(window, play_button_sprite, 'play', 380, 500, True)
    BUTTONS.append(play_button)

    quit_sprite = pygame.image.load('sprites/main_menu/quit_button.png').convert()
    quit_button = Button(window, quit_sprite, 'quit', 700, 500, True)
    BUTTONS.append(quit_button)

    options_sprite = pygame.image.load('sprites/main_menu/options_button.png').convert()
    options_button = Button(window, options_sprite, 'options', 60, 500, True)
    BUTTONS.append(options_button)

    stages_sprite = pygame.image.load('sprites/main_menu/stages.png').convert_alpha()
    stages_button = Button(window, stages_sprite, 'none', 0, 5, False)
    BUTTONS.append(stages_button)
    LEVEL_BUTTONS.append(stages_button)

    stage1_sprite = pygame.image.load('sprites/main_menu/stage1.png').convert_alpha()
    stage1_button = Button(window, stage1_sprite, 'stage1', 0, 70, False)
    BUTTONS.append(stage1_button)
    LEVEL_BUTTONS.append(stage1_button)

    stage2_sprite = pygame.image.load('sprites/main_menu/stage2.png').convert_alpha()
    stage2_button = Button(window, stage2_sprite, 'stage2', 0, 130, False)
    BUTTONS.append(stage2_button)
    LEVEL_BUTTONS.append(stage2_button)

    stage3_sprite = pygame.image.load('sprites/main_menu/stage3.png').convert_alpha()
    stage3_button = Button(window, stage3_sprite, 'stage3', 0, 190, False)
    BUTTONS.append(stage3_button)
    LEVEL_BUTTONS.append(stage3_button)

    stage4_sprite = pygame.image.load('sprites/main_menu/stage4.png').convert_alpha()
    stage4_button = Button(window, stage4_sprite, 'stage4', 0, 250, False)
    BUTTONS.append(stage4_button)
    LEVEL_BUTTONS.append(stage4_button)

    stage5_sprite = pygame.image.load('sprites/main_menu/stage5.png').convert_alpha()
    stage5_button = Button(window, stage5_sprite, 'stage5', 0, 310, False)
    BUTTONS.append(stage5_button)
    LEVEL_BUTTONS.append(stage5_button)

    stage6_sprite = pygame.image.load('sprites/main_menu/stage6.png').convert_alpha()
    stage6_button = Button(window, stage6_sprite, 'stage6', 0, 370, False)
    BUTTONS.append(stage6_button)
    LEVEL_BUTTONS.append(stage6_button)

    options_bg_sprite = pygame.image.load('sprites/main_menu/options_background.png').convert_alpha()
    options_bg = Button(window, options_bg_sprite, 'none', 250, 50, False) #Does nothing
    BUTTONS.append(options_bg)
    OPTIONS_BUTTONS.append(options_bg)

    credits_sprite = pygame.image.load('sprites/main_menu/credits.png').convert_alpha()
    credits = Button(window, credits_sprite, 'none', 270, 180, False) #Does nothing
    BUTTONS.append(credits)
    OPTIONS_BUTTONS.append(credits)

    controls_sprite = pygame.image.load('sprites/main_menu/controls.png').convert_alpha()
    controls_button = Button(window, controls_sprite, 'none', 630, 330, False)
    BUTTONS.append(controls_button)
    OPTIONS_BUTTONS.append(controls_button)

    toggle_sound_sprite = pygame.image.load('sprites/main_menu/toggle_sound.png').convert()
    sound_button = Button(window, toggle_sound_sprite, 'sound_toggle', 300, 100, False)
    BUTTONS.append(sound_button)
    OPTIONS_BUTTONS.append(sound_button)

    stat_bg_sprite = pygame.image.load('sprites/main_menu/options_background.png').convert()
    stat_bg_button = Button(window, stat_bg_sprite, 'none', 247, 100, False)
    BUTTONS.append(stat_bg_button)
    STATS_BUTTONS.append(stat_bg_button)

    close_button_sprite = pygame.image.load('sprites/main_menu/close_button.png').convert()
    close_button = Button(window, close_button_sprite, 'close', 380, 314, False)
    BUTTONS.append(close_button)
    STATS_BUTTONS.append(close_button)

    #Used to display round statistics
    med_font = pygame.font.Font('freesansbold.ttf', 30)
    large_font = pygame.font.Font('freesansbold.ttf', 45)
    score = 0
    kills = 0
    distance = 0
    score_text = med_font.render('Score: {}'.format(score), True, (255, 255, 255) )
    kills_text = med_font.render('Kills: {}'.format(kills), True, (255, 255, 255) )
    distance_text = med_font.render('Distance Travelled: {} km'.format(distance), True, (255, 255, 255) )
    paused_text = large_font.render('Game Paused', True, (255, 255, 255) )

    #Main Menu Music
    if SOUNDS_ON == True:
        pygame.mixer.music.load('sounds/music/main_menu_music.wav')
        pygame.mixer.music.play(-1)

    running = True #USED FOR THE MAIN GAME LOOP
    menu_on = True #USED FOR THE MENU LOOP
    paused = False #Used to pause the game


    #GAME LOOP------------------------------------------------------------------
    while running:

        while menu_on: #Main menu loop------------------------------------------

            window.blit(menu_bg, (0, 0) )

            for event in pygame.event.get(): #MENU EVENT LOOP
                if event.type == pygame.QUIT: #Check if player quit
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    check_buttons()

            for button in BUTTONS:
                button.draw()

            menu_on = check_stage_selected(player)
            clock.tick(fps)#Tick fps

            #check for an active level
            current_level = check_level_active()
            level_end_timer = get_level_end_timer(current_level)

            if SHOWING_STATS == True:
                #Create text
                window.blit(score_text, (430, 150) )
                window.blit(kills_text, (440, 190) )
                window.blit(distance_text, (320, 230) )

            pygame.display.update()

        bg = update_background(current_level)[0]
        fg = update_background(current_level)[1]


        #END OF MAIN MENU LOOP-------------------------------------------------

        #Bring Back the main menu if level is over, or if player is dead
        if level_end_timer <= 0 or player.get_health() <= 0 or len(ENEMY_LIST) <= 0:
            for object in STATS_BUTTONS:
                object.toggle_visibility()
            #Stat setup/ update
            score = player.get_score()
            kills = player.get_kills()
            distance = player.get_distance()
            score_text = med_font.render('Score: {}'.format(score), True, (255, 255, 255) )
            kills_text = med_font.render('Kills: {}'.format(kills), True, (255, 255, 255) )
            distance_text = med_font.render('Distance Travelled: {} km'.format(distance), True, (255, 255, 255) )
            #Reset reset stats and position
            SHOWING_STATS = True
            player.reset_multiplier()
            player.reset_stats()
            player.reset_position()
            PROJECTILES.clear()
            #cleanup enemies
            for enemy in ENEMY_LIST:
                enemy.kill_self()
            #stop music and return the menu and buttons
            mixer.music.stop()
            if SOUNDS_ON == True:
                pygame.mixer.music.load('sounds/music/main_menu_music.wav')
                pygame.mixer.music.play(-1)
            for button in BUTTONS:
                if button.get_type() == 'options' or button.get_type() == 'quit' or button.get_type() == 'play':
                    button.return_to_screen()

            menu_on = True

        if paused == False: #Check if paused before updating the backgrounds
            #Background scrolling/drawing setup
            bg_x -= 0.6
            bg_x2 -= 0.6

            if bg_x < bg.get_width() * -1:
                bg_x = bg.get_width()
            if bg_x2 < bg.get_width() * -1:
                bg_x2 = bg.get_width()

            ps_x  -= 1
            ps_x2 -= 1

            if ps_x < bg.get_width() * -1:
                ps_x = bg.get_width()
            if ps_x2 < bg.get_width() * -1:
                ps_x2 = bg.get_width()

        draw_bg(window, bg, bg_x, bg_x2)
        draw_passing_stars(window, fg, ps_x, ps_x2)

        for event in pygame.event.get(): #EVENT LOOP----------------------------
            if event.type == pygame.QUIT: #Check if player quit
                running = False

            elif event.type == pygame.KEYDOWN: #Key presses

                if event.key == pygame.K_a: #MOVEMENT--------------------------
                    player_xChange = -5
                    player.switch_active_animation(3, 0)

                    if pygame.key.get_pressed()[pygame.K_w] == 1: #check if moving up
                        player.switch_active_animation(4, 0)
                    if pygame.key.get_pressed()[pygame.K_s] == 1: #check if moving backwards
                        player.switch_active_animation(5, 0)

                elif event.key == pygame.K_d:
                    player_xChange = 5
                    player.switch_active_animation(0, 0)

                elif event.key == pygame.K_w:
                    player_yChange = -5
                    player.switch_active_animation(1, 0)

                    if pygame.key.get_pressed()[pygame.K_a] == 1: #check if moving backwards
                        player.switch_active_animation(4, 0)

                elif event.key == pygame.K_s:
                    player_yChange = 5
                    player.switch_active_animation(2, 0)

                    if pygame.key.get_pressed()[pygame.K_a] == 1: #check if moving backwards
                        player.switch_active_animation(5, 0)


                elif event.key == pygame.K_SPACE:
                    if WEAPON_READY == True:
                        player.shoot_main()
                        WEAPON_READY = False
                    else:
                        pass
                elif event.key == pygame.K_ESCAPE:
                    if paused == False:
                        mixer.music.pause()
                        paused = True
                    else:
                        mixer.music.unpause()
                        paused = False

            elif event.type == pygame.KEYUP: #Key releases

                if event.key == pygame.K_a:
                    if pygame.key.get_pressed()[pygame.K_d] == 0: #Check opp key (0 = not pressed)
                        player_xChange = 0
                        player.switch_active_animation(0, 0)
                    else:
                        player_xChange = 5
                        player.switch_active_animation(0, 0)

                    if pygame.key.get_pressed()[pygame.K_w] == 1: #Check if going upward
                        player.switch_active_animation(1, 0)
                    elif pygame.key.get_pressed()[pygame.K_s] == 1: #Check if going upward
                        player.switch_active_animation(2, 0)

                elif event.key == pygame.K_d:
                    if pygame.key.get_pressed()[pygame.K_a] == 0: #check opp key
                        player_xChange = 0
                        player.switch_active_animation(0, 0)
                    else:
                        player_xChange = -5
                        player.switch_active_animation(3, 0)

                    if pygame.key.get_pressed()[pygame.K_w] == 1: #Check if going upward
                        player.switch_active_animation(1, 0)
                    elif pygame.key.get_pressed()[pygame.K_s] == 1: #Check if going upward
                        player.switch_active_animation(2, 0)

                elif event.key == pygame.K_w:
                    if pygame.key.get_pressed()[pygame.K_s] == 0: #check opp key
                        player_yChange = 0
                        player.switch_active_animation(0, 0)
                    else:
                        player_yChange = 5
                        player.switch_active_animation(2, 0) #play down anim

                    if pygame.key.get_pressed()[pygame.K_a] == 1: #Check if moving backwards
                        player.switch_active_animation(3, 0)

                elif event.key == pygame.K_s:
                    if pygame.key.get_pressed()[pygame.K_w] == 0: #check opp key
                        player_yChange = 0
                        player.switch_active_animation(0, 0)
                    else:
                        player_yChange = -5
                        player.switch_active_animation(1, 0) #play up anim

                    if pygame.key.get_pressed()[pygame.K_a] == 1: #Check if moving backwards
                        player.switch_active_animation(3, 0)


        if paused == False: #Check if pasued before updates etc.
            #Handle weapon cooldown
            handle_weapon_cooldown()

            player_x += player_xChange #Change location
            player_y += player_yChange
            #Update distance for stats
            player.add_distance(player_xChange)
            player.add_distance(player_yChange)
            #Check if player is in-bounds
            if player_x <= -2:
                player_x = -2
            elif player_x >= 860:
                player_x = 860
            if player_y <= -5:
                player_y = -5
            elif player_y >= 640:
                player_y = 640

            clock.tick(fps)#Tick fps
            boundary_check(player, explosions)
            check_collisions(player, explosions, window, SOUNDS_ON)
            update(player, player_x, player_y, window, explosions)#update drawing locations
            level_end_timer = update_level_timer(level_end_timer)

        elif paused == True:
            window.blit(paused_text, (350, 300))
            pygame.display.update()


if __name__ == "__main__":
    main()
