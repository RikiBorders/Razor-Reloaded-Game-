#This file holds all enemy objects.
#Enemies can have sprite sequences, or any other amount of sprites.
#Sprite counter will be noted in the class doc-string.
#IMPORTANT FOR SPAWN TIMER: 500 = 1 second

import pygame
import random
from sprite_sequences import *
from main import *

pygame.init()

ENEMY_SOUNDS = {}
ENEMY_SOUNDS['asteroid_destruction_sound'] = mixer.Sound('sounds/sound_effects/asteroid_destruction.wav')
ENEMY_SOUNDS['asteroid_collision_sound'] = mixer.Sound('sounds/sound_effects/asteroid_collision.wav')
ENEMY_SOUNDS['barrel_explosion'] = mixer.Sound('sounds/sound_effects/barrel_explosion.wav')
ENEMY_SOUNDS['fighter_damaged'] = mixer.Sound('sounds/sound_effects/fighter_damaged.wav')
ENEMY_SOUNDS['enemy_shoot_sound'] = mixer.Sound('sounds/sound_effects/fighter_laser.wav')
ENEMY_SOUNDS['battleship_damaged'] = mixer.Sound('sounds/sound_effects/battleship_damaged.wav')


class Asteroid1():
    '''70x70 asteroid (single sprite)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for asteroid1'''
        asteroid_health = [10, 20]
        rotation_speeds = [ 0.2, 0.4, 0.6, 0.8, 1, 1.5, 1.8]
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = random.choice(asteroid_health)
        self._alive = True
        self._velocity = -3
        self._vertical_velocity = -0.5
        self._top_boundary = self._ypos + 50
        self._bottom_boundary = self._ypos - 50
        self._sprite = enemy_dictionary.get(sprite)
        self._spawn_time = spawn_time
        self._type = 'asteroid'
        self._score_val = 10
        self._hitbox = (self._xpos + 16, self._ypos + 15, 65, 65)

        #Rotation
        self._original_sprite = enemy_dictionary.get(sprite)
        self._rotation = random.choice(rotation_speeds)

    def __str__(self):
        '''String method'''
        return 'Asteroid with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Asteroid with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def draw(self):
        '''Draw the asteroid to the screen'''
        self._sprite = pygame.transform.rotate(self._original_sprite, self._rotation)
        self._rotation += 0.4
        self._window.blit(self._sprite, (self._xpos, self._ypos))
        self._hitbox = (self._xpos + 16, self._ypos + 15, 55, 55)
        if self._spawn_time <= 0:

            #correct vertical boundaries if out of bounds
            if self._bottom_boundary <= 10:
                self._bottom_boundary = 10
            if self._top_boundary >= 680:
                self._top_boundary = 680
            #Handle y-movement
            self._ypos += self._vertical_velocity

            if self._ypos >= self._top_boundary:
                self._vertical_velocity = -0.5
            elif self._ypos <= self._bottom_boundary:
                self._vertical_velocity = 0.5

            self._xpos += self._velocity

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:
                #Create explosion at impact
                make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['asteroid_destruction_sound'].play()
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()
                else:
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['asteroid_collision_sound'].play()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class Asteroid2():
    '''140x140 asteroid (single sprite)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for asteroid1'''
        asteroid_health = [30, 40, 45]
        rotation_speeds = [0.1, 0.3, 0.6, 0.9, 1.4, 1.8]
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = random.choice(asteroid_health)
        self._alive = True
        self._velocity = -2
        self._sprite = enemy_dictionary.get(sprite)
        self._type = 'asteroid2'
        self._score_val = 10
        self._spawn_time = spawn_time
        self._hitbox = (self._xpos + 22, self._ypos + 30, 140, 140)
        self._alive = True

        #Rotation
        self._original_sprite = enemy_dictionary.get(sprite)
        self._rotation = random.choice(rotation_speeds)

    def __str__(self):
        '''String method'''
        return 'Asteroid with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Asteroid with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def draw(self):
        '''Draw the asteroid to the screen'''
        self._sprite = pygame.transform.rotate(self._original_sprite, self._rotation)
        self._rotation += 0.4
        self._window.blit(self._sprite, (self._xpos, self._ypos))
        self._hitbox = (self._xpos + 22, self._ypos + 30, 120, 120)
        if self._spawn_time <= 0:
            self._xpos += self._velocity

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:
                #Create explosion at impact
                make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['asteroid_destruction_sound'].play()
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()
                else:
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['asteroid_collision_sound'].play()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class Barrel1():
    '''40x70 Barrel (single sprite)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for barrel1'''
        rotation_speeds = [1, 2.3, 3]
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = 10
        self._alive = True
        self._velocity = -2
        self._sprite = enemy_dictionary.get(sprite)
        self._type = 'barrel'
        self._score_val = 5
        self._spawn_time = spawn_time
        self._hitbox = (self._xpos + 6, self._ypos + 15, 40, 66)
        self._alive = True

        #Rotation variables
        self._original_sprite = enemy_dictionary.get(sprite)
        self._rotation = random.choice(rotation_speeds)

    def __str__(self):
        '''String method'''
        return 'Barrel with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Barrel with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def draw(self):
        '''Draw the Barrel to the screen'''
        self._sprite = pygame.transform.rotate(self._original_sprite, self._rotation)
        self._rotation += 1

        self._window.blit(self._sprite, (self._xpos, self._ypos))
        self._hitbox = (self._xpos + 6, self._ypos + 15, 40, 66)
        if self._spawn_time <= 0:
            self._xpos += self._velocity

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                #Create explosion at impact
                make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['barrel_explosion'].play()
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class Fighter1():
    '''120x70 Fighter (sequence)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor fighter1'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = 40
        self._alive = True
        self._velocity = -2
        self._cooldown = 3240
        self._weapon_ready = True
        self._spawn_time = spawn_time
        self._sprite = enemy_dictionary.get(sprite)
        self._bullet = projectile_dictionary.get('enemy_laser')
        self._type = 'fighter'
        self._score_val = 40
        self._hitbox = (self._xpos, self._ypos, 115, 70)
        self._projectiles = []
        self._alive = True
        #Animation
        self._frame_counter = 500
        self._frame_index = 0 #which frame in a sequence

    def __str__(self):
        '''String method'''
        return 'Fighter with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Fighter with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def draw(self):
        '''Draw to the screen'''
        self._window.blit(self._sprite[self._frame_index], (self._xpos, self._ypos))
        self._hitbox = (self._xpos, self._ypos, 115, 70)
        if self._spawn_time <= 0:
            self._xpos += self._velocity

        #Update frame counter, and active animation sequence frame
        if self._frame_counter > 0:
            self._frame_counter -= 50 #Higher # = faster switch
        else:
            self._frame_index += 1
            if self._frame_index >= len(self._sprite):
                self._frame_index = 0
            self._frame_counter = 400

        #Handle projectile shooting
        for projectile in self._projectiles:
            projectile.update()

            if projectile.get_xpos() <= 0:
                if projectile in self._projectiles:
                    self._projectiles.remove(projectile)

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def handle_cooldown(self):
        '''handle the weapon's cooldown'''
        #Handle laser shooting
        if self._weapon_ready == True:
            self.shoot()
        else:
            self._cooldown -= 20
            if self._cooldown <= 0:
                self._weapon_ready = True

    def shoot(self, SOUNDS_ON, projectile_list):
        '''periodically fire bullets'''
        if self._weapon_ready == True:
            if SOUNDS_ON == True:
                ENEMY_SOUNDS['enemy_shoot_sound'].play()
            enemy_bullet = Projectile(self._window, (self._xpos, self._ypos + 28), -5, self._bullet, 15)
            self._projectiles.append(enemy_bullet)
            projectile_list.append(enemy_bullet)
            enemy_bullet.update()
            self._weapon_ready = False
            self._cooldown = 3240
        #Handle cooldown
        else:
            self._cooldown -= 20
            if self._cooldown <= 0:
                self._weapon_ready = True

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                #Create explosion at impact
                make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                #Damage sound
                if SOUNDS_ON == True:
                    ENEMY_SOUNDS['fighter_damaged'].play()
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class Shielder1():
    '''110x54 Shielder (sequence)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for Shielder1'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = 60
        self._alive = True
        self._velocity = -2
        self._cooldown = 2500
        self._weapon_ready = True
        self._spawn_time = spawn_time
        self._sprite = enemy_dictionary.get(sprite)
        self._type = 'shielder'
        self._hitbox = (self._xpos, self._ypos, 110, 50)
        self._alive = True
        self._score_val = 30
        self._impact_sound = mixer.Sound('sounds/sound_effects/shield_impact.wav')
        self._explosion_elapsed = False

        #Animation
        self._frame_counter = 500
        self._frame_index = 0 #which frame in a sequence

    def __str__(self):
        '''String method'''
        return 'Shielder with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Shielder with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def draw(self):
        '''Draw to the screen'''
        self._window.blit(self._sprite[self._frame_index], (self._xpos, self._ypos))
        self._hitbox = (self._xpos, self._ypos, 110, 50)
        if self._spawn_time <= 0:
            self._xpos += self._velocity

        #Update frame counter, and active animation sequence frame
        if self._frame_counter > 0:
            self._frame_counter -= 50 #Higher # = faster switch
        else:
            self._frame_index += 1
            if self._frame_index >= len(self._sprite):
                self._frame_index = 0
            self._frame_counter = 400

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''

        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                #Create explosion at impact
                make_shield_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                if SOUNDS_ON == True:
                    self._impact_sound.play()
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    if SOUNDS_ON == True:
                        ENEMY_SOUNDS['battleship_damaged'].play()
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class Tracker1():
    '''60x30 Tracker (sequence)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for Shielder1'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = 15
        self._alive = True
        self._velocity = -3
        self._vertical_velocity = -2
        self._top_boundary = self._ypos + 100
        self._bottom_boundary = self._ypos - 100
        self._cooldown = 4000
        self._weapon_ready = True
        self._spawn_time = spawn_time
        self._bullet = projectile_dictionary.get('plasma_laser')
        self._projectiles = []
        self._sprite = enemy_dictionary.get(sprite)
        self._type = 'tracker'
        self._score_val = 15
        self._hitbox = (self._xpos, self._ypos, 60, 40)
        self._alive = True
        self._shoot_sound = mixer.Sound('sounds/sound_effects/tracker_laser.wav')
        self._damage_sound = mixer.Sound('sounds/sound_effects/tracker_explosion.wav')

        #Animation
        self._frame_counter = 500
        self._frame_index = 0 #which frame in a sequence

    def __str__(self):
        '''String method'''
        return 'Tracker with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Tracker with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def draw(self):
        '''Draw to the screen'''
        #Draw the sprite and hitbox
        self._window.blit(self._sprite[self._frame_index], (self._xpos, self._ypos))
        self._hitbox = (self._xpos, self._ypos, 60, 30)
        #start movement after its assigned 'spawn' time
        if self._spawn_time <= 0:
            self._xpos += self._velocity

            #correct vertical boundaries if out of bounds
            if self._bottom_boundary <= 10:
                self._bottom_boundary = 10
            if self._top_boundary >= 680:
                self._top_boundary = 680
            #Handle y-movement
            self._ypos += self._vertical_velocity

            if self._ypos >= self._top_boundary:
                self._vertical_velocity = -2
            elif self._ypos <= self._bottom_boundary:
                self._vertical_velocity = 2

        #Update frame counter, and active animation sequence frame
        if self._frame_counter > 0:
            self._frame_counter -= 50 #Higher # = faster switch
        else:
            self._frame_index += 1
            if self._frame_index >= len(self._sprite):
                self._frame_index = 0
            self._frame_counter = 400

        #Handle projectile shooting
        for projectile in self._projectiles:
            projectile.update()

            if projectile.get_xpos() <= 0:
                if projectile in self._projectiles:
                    self._projectiles.remove(projectile)

    def shoot(self, SOUNDS_ON, projectile_list):
        '''periodically fire bullets'''
        if self._weapon_ready == True:
            if SOUNDS_ON == True:
                self._shoot_sound.play()
            enemy_bullet = Projectile(self._window, (self._xpos, self._ypos + 6), -5, self._bullet, 10)
            self._projectiles.append(enemy_bullet)
            projectile_list.append(enemy_bullet)
            enemy_bullet.update()
            self._weapon_ready = False
            self._cooldown = 4000
        else:
            self._cooldown -= 20
            if self._cooldown <= 0:
                self._weapon_ready = True

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                #Create explosion at impact
                make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                if SOUNDS_ON == True:
                    self._damage_sound.play()
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class EvilEye():
    '''120x65 Evil Eye (sequence)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for Evil Eye'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = 30
        self._alive = True
        self._velocity = -4
        self._vertical_velocity = -1
        self._top_boundary = self._ypos + 45
        self._bottom_boundary = self._ypos - 45
        self._cooldown = 3800
        self._weapon_ready = True
        self._spawn_time = spawn_time
        self._bullet = projectile_dictionary.get('eye_laser')
        self._projectiles = []
        self._sprite = enemy_dictionary.get(sprite)
        self._type = 'evil_eye'
        self._score_val = 15
        self._hitbox = (self._xpos, self._ypos, 120, 65)
        self._alive = True
        self._shoot_sound = mixer.Sound('sounds/sound_effects/eye_laser.wav')
        self._damage_sound = mixer.Sound('sounds/sound_effects/eye_damaged.wav')

        #Animation
        self._frame_counter = 500
        self._frame_index = 0 #which frame in a sequence

    def __str__(self):
        '''String method'''
        return 'Tracker with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Tracker with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def draw(self):
        '''Draw to the screen'''
        #Draw the sprite and hitbox
        self._window.blit(self._sprite[self._frame_index], (self._xpos, self._ypos))
        self._hitbox = (self._xpos, self._ypos, 120, 65)
        #start movement after its assigned 'spawn' time
        if self._spawn_time <= 0:
            self._xpos += self._velocity

            #correct vertical boundaries if out of bounds
            if self._bottom_boundary <= 10:
                self._bottom_boundary = 10
            if self._top_boundary >= 650:
                self._top_boundary = 650
            #Handle y-movement
            self._ypos += self._vertical_velocity

            if self._ypos >= self._top_boundary:
                self._vertical_velocity = -2
            elif self._ypos <= self._bottom_boundary:
                self._vertical_velocity = 2

        #Update frame counter, and active animation sequence frame
        if self._frame_counter > 0:
            self._frame_counter -= 50 #Higher # = faster switch
        else:
            self._frame_index += 1
            if self._frame_index >= len(self._sprite):
                self._frame_index = 0
            self._frame_counter = 400

        #Handle projectile shooting
        for projectile in self._projectiles:
            projectile.update()

            if projectile.get_xpos() <= 0:
                if projectile in self._projectiles:
                    self._projectiles.remove(projectile)

    def shoot(self, SOUNDS_ON, projectile_list):
        '''periodically fire bullets'''
        if self._weapon_ready == True:
            if SOUNDS_ON == True:
                self._shoot_sound.play()
            enemy_bullet = Projectile(self._window, (self._xpos, self._ypos + 6), -5, self._bullet, 10)
            self._projectiles.append(enemy_bullet)
            projectile_list.append(enemy_bullet)
            enemy_bullet.update()
            self._weapon_ready = False
            self._cooldown = 3800
        else:
            self._cooldown -= 20
            if self._cooldown <= 0:
                self._weapon_ready = True

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                #Create explosion at impact
                make_eye_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                if SOUNDS_ON == True:
                    self._damage_sound.play()
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class Battleship():
    '''240x130 Battleship (sequence)'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for Battleship'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._health = 500
        self._alive = True
        self._velocity = -2
        self._cooldown = 1600
        self._weapon_ready = True
        self._music_flag = False #Used to indicate when to start boss music
        self._spawn_time = spawn_time
        self._sprite = enemy_dictionary.get(sprite)
        self._bullet = projectile_dictionary.get('battleship_laser')
        self._bullet2 = projectile_dictionary.get('battleship_laser2')
        self._type = 'battleship'
        self._cannon_sound = mixer.Sound('sounds/sound_effects/battleship_fire.wav')
        self._score_val = 5000
        self._hitbox = (self._xpos, self._ypos, 240, 130)
        self._projectiles = []
        self._alive = True
        #Animation
        self._frame_counter = 500
        self._frame_index = 0 #which frame in a sequence

    def __str__(self):
        '''String method'''
        return 'Battleship with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Battleship with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def get_health(self):
        '''Return the enemy's health'''
        return self._health

    def draw(self):
        '''Draw to the screen'''
        self._window.blit(self._sprite[self._frame_index], (self._xpos, self._ypos))
        self._hitbox = (self._xpos, self._ypos, 240, 130)
        if self._spawn_time <= 0:
            self._xpos += self._velocity

        #Stop movement when on screen
        if self._xpos <= 750:
            self._velocity = 0

        #Update frame counter, and active animation sequence frame
        if self._frame_counter > 0:
            self._frame_counter -= 50 #Higher # = faster switch
        else:
            self._frame_index += 1
            if self._frame_index >= len(self._sprite):
                self._frame_index = 0
            self._frame_counter = 400

        #Handle projectile shooting
        for projectile in self._projectiles:
            projectile.update()

            if projectile.get_xpos() <= 0:
                if projectile in self._projectiles:
                    self._projectiles.remove(projectile)

    def get_type(self):
        '''Return the enmy's type'''
        return self._type

    def handle_cooldown(self):
        '''handle the weapon's cooldown'''
        #Handle laser shooting
        if self._weapon_ready == True:
            self.shoot()
        else:
            self._cooldown -= 20
            if self._cooldown <= 0:
                self._weapon_ready = True

    def shoot(self, SOUNDS_ON, projectile_list):
        '''periodically fire bullets'''
        #Shoot 3 bullets
        if self._weapon_ready == True:
            if SOUNDS_ON == True:
                self._cannon_sound.play()
            #Top bullet
            enemy_bullet1 = Projectile(self._window, (self._xpos, self._ypos + 20), -5, self._bullet, 30)
            self._projectiles.append(enemy_bullet1)
            projectile_list.append(enemy_bullet1)

            #Bottom bullet
            enemy_bullet2 = Projectile(self._window, (self._xpos, self._ypos + 88), -5, self._bullet, 30)
            self._projectiles.append(enemy_bullet2)
            projectile_list.append(enemy_bullet2)

            #Middle bullet
            enemy_bullet3 = Projectile(self._window, (self._xpos, self._ypos + 60), -6, self._bullet2, 40)
            self._projectiles.append(enemy_bullet3)
            projectile_list.append(enemy_bullet3)

            self._weapon_ready = False
            self._cooldown = 1600
        #Handle cooldown
        else:
            self._cooldown -= 20
            if self._cooldown <= 0:
                self._weapon_ready = True

        #Handle boss music
        if SOUNDS_ON == True:
            if self._music_flag == False:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music/battleship_music.wav')
                pygame.mixer.music.play(-1)
                self._music_flag = True

    def check_collision(self, projectile, player, explosion_list, SOUNDS_ON):
        '''check for collision'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                #Create explosion at impact
                make_impact_explosion(self._window, projectile.get_xpos(), projectile.get_ypos(), explosion_list)
                #Damage sound
                if SOUNDS_ON == True:
                    ENEMY_SOUNDS['battleship_damaged'].play()
                #Cleanup bullet
                player.remove_bullet(projectile)
                projectile.move_offscreen()
                self._health -= projectile.get_damage()

                #Handle enemy death
                if self._health <= 0:
                    player.add_score(self._score_val) #Add enemy score value to the score
                    self._explosion_x = self._xpos
                    self._explosion_y = self._ypos
                    self.kill_self()
                    player.add_kill()
                    player.add_multiplier()

    def get_explosion_cords(self):
        '''return coordinates for the explosion'''
        return (self._explosion_x, self._explosion_y)

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10


class HealthPack():
    '''64x64 Health Pack'''

    def __init__(self, window, xpos, ypos, sprite, spawn_time):
        '''Constructor for Health Pack'''
        self._window = window
        self._xpos = xpos
        self._ypos = ypos
        self._alive = True
        self._velocity = -3
        self._spawn_time = spawn_time
        self._sprite = sprite
        self._type = 'health_pack'
        self._hitbox = (self._xpos, self._ypos, 66, 69)
        self._alive = True
        self._sound_effect = mixer.Sound('sounds/sound_effects/health_grabbed.wav')

        self._rotation = 1
        self._original_sprite = self._sprite

    def __str__(self):
        '''String method'''
        return 'Tracker with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def __repr__(self):
        '''List representation'''
        return 'Tracker with velocity {} at {}, {}'.format(self._velocity, self._xpos, self._ypos)

    def get_spawn_timer(self):
        '''return enemy spawn timer'''
        return self._spawn_time

    def draw(self):
        '''Draw to the screen'''
        #Draw the sprite and hitbox
        self._window.blit(self._sprite, (self._xpos, self._ypos) )
        self._sprite = pygame.transform.rotate(self._original_sprite, self._rotation)
        self._rotation += 0.2

        self._hitbox = (self._xpos, self._ypos, 64, 69)
        #start movement after its assigned 'spawn' time
        if self._spawn_time <= 0:
            self._xpos += self._velocity

    def get_type(self):
        '''Return the object's type'''
        return self._type

    def check_grabbed(self, player, projectile, SOUNDS_ON):
        '''check if health pack was grabbed'''
        if projectile.get_ypos() < self._hitbox[1] + self._hitbox[3] and projectile.get_ypos() > self._hitbox[1]:
            if projectile.get_xpos() > self._hitbox[0] and projectile.get_xpos() < self._hitbox[0] + self._hitbox[2]:

                if SOUNDS_ON == True:
                    self._sound_effect.play()
                #Add 40 to player health
                player.add_health(40)
                self.kill_self()

    def kill_self(self):
        '''kill and cleanup the enemy'''
        self._velocity = 0
        self._xpos = 5000
        self._alive = False

    def is_alive(self):
        '''Return if alive or not'''
        if self._alive == True:
            return True
        else:
            return False

    def get_xpos(self):
        '''Return x position'''
        return self._xpos

    def get_ypos(self):
        '''Return y position'''
        return self._ypos

    def reduce_spawn_timer(self):
        '''Update enemy spawn timer'''
        self._spawn_time -= 10
