#Sprite lists for animations
import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))

#Player movement animation grid. each row = sequence, and each column = frame
player_animations = []
#Sequence indecies:
#[0] is the forward/idle animation sequence
#[1] is the upward sequence
#[2] is the downward sequence
#[3] is the backward sequence
#[4] is the backward/up sequence
#[5] is the backward/down sequence

#Each frame is 120x65 pixels. The ship's leftmost point is 1 pixel from the border,
#The ship's middle-bottom thruster's lowest black pixel is 11 pixels from the
#bottom border

#Player forward sequences
player_fwd_animation = [] #4 frames
player_animations.append(player_fwd_animation)

f1 = pygame.image.load('sprites/player_sprites/player_fwd1.png').convert_alpha()
player_fwd_animation.append(f1)
f2 = pygame.image.load('sprites/player_sprites/player_fwd2.png').convert_alpha()
player_fwd_animation.append(f2)
f3 = pygame.image.load('sprites/player_sprites/player_fwd3.png').convert_alpha()
player_fwd_animation.append(f3)
f4 = pygame.image.load('sprites/player_sprites/player_fwd4.png').convert_alpha()
player_fwd_animation.append(f4)

#Player upward sequences
player_up_animation = [] #4 frames
player_animations.append(player_up_animation)

u1 = pygame.image.load('sprites/player_sprites/player_up1.png').convert_alpha()
player_up_animation.append(u1)
u2 = pygame.image.load('sprites/player_sprites/player_up2.png').convert_alpha()
player_up_animation.append(u2)
u3 = pygame.image.load('sprites/player_sprites/player_up3.png').convert_alpha()
player_up_animation.append(u3)
u4 = pygame.image.load('sprites/player_sprites/player_up4.png').convert_alpha()
player_up_animation.append(u4)

#Player downward sequences
player_down_animation = [] #4 frames
player_animations.append(player_down_animation)

u1 = pygame.image.load('sprites/player_sprites/player_down1.png').convert_alpha()
player_down_animation.append(u1)
u2 = pygame.image.load('sprites/player_sprites/player_down2.png').convert_alpha()
player_down_animation.append(u2)
u3 = pygame.image.load('sprites/player_sprites/player_down3.png').convert_alpha()
player_down_animation.append(u3)
u4 = pygame.image.load('sprites/player_sprites/player_down4.png').convert_alpha()
player_down_animation.append(u4)

#Player backward sequences
player_back_animation = [] #4 frames
player_animations.append(player_back_animation)

b1 = pygame.image.load('sprites/player_sprites/player_back1.png').convert_alpha()
player_back_animation.append(b1)
b2 = pygame.image.load('sprites/player_sprites/player_back2.png').convert_alpha()
player_back_animation.append(b2)
b3 = pygame.image.load('sprites/player_sprites/player_back3.png').convert_alpha()
player_back_animation.append(b3)
b4 = pygame.image.load('sprites/player_sprites/player_back4.png').convert_alpha()
player_back_animation.append(b4)

#Player backward-upward sequences
player_back_up_animation = [] #4 frames
player_animations.append(player_back_up_animation)

bu1 = pygame.image.load('sprites/player_sprites/player_back_up1.png').convert_alpha()
player_back_up_animation.append(bu1)
bu2 = pygame.image.load('sprites/player_sprites/player_back_up2.png').convert_alpha()
player_back_up_animation.append(bu2)
bu3 = pygame.image.load('sprites/player_sprites/player_back_up3.png').convert_alpha()
player_back_up_animation.append(bu3)
bu4 = pygame.image.load('sprites/player_sprites/player_back_up4.png').convert_alpha()
player_back_up_animation.append(bu4)

#Player backward-downward sequences
player_back_down_animation = [] #4 frames
player_animations.append(player_back_down_animation)

bd1 = pygame.image.load('sprites/player_sprites/player_down_back1.png').convert_alpha()
player_back_down_animation.append(bd1)
bd2 = pygame.image.load('sprites/player_sprites/player_down_back2.png').convert_alpha()
player_back_down_animation.append(bd2)
bd3 = pygame.image.load('sprites/player_sprites/player_down_back3.png').convert_alpha()
player_back_down_animation.append(bd3)
bd4 = pygame.image.load('sprites/player_sprites/player_down_back4.png').convert_alpha()
player_back_down_animation.append(bd4)


#Projectile dictionary (not animated)
projectile_dictionary = {}
#Sequence indexes:
#['bullet'] is the bullet sprite 20x11
#['enemy_laser'] is the enemy laser sprite 25x11
#['plasma_laser'] is the tracker laser ball 20x20


#each projectile is of different size, but 20 x 11 is standard
bullet_sprite = pygame.image.load('sprites/projectiles/projectile_bullet.png').convert_alpha()
projectile_dictionary['bullet'] = bullet_sprite

enemy_laser_sprite = pygame.image.load('sprites/projectiles/enemy_laser.png').convert_alpha()
projectile_dictionary['enemy_laser'] = enemy_laser_sprite

plasma_laser_sprite = pygame.image.load('sprites/projectiles/plasma_laser.png').convert_alpha()
projectile_dictionary['plasma_laser'] = plasma_laser_sprite

eye_laser_sprite = pygame.image.load('sprites/projectiles/eye_laser.png').convert_alpha()
projectile_dictionary['eye_laser'] = eye_laser_sprite

battleship_laser_sprite = pygame.image.load('sprites/projectiles/battleship_laser1.png').convert_alpha()
projectile_dictionary['battleship_laser'] = battleship_laser_sprite

battleship_laser_sprite2 = pygame.image.load('sprites/projectiles/battleship_laser2.png').convert_alpha()
projectile_dictionary['battleship_laser2'] = battleship_laser_sprite2

drone_laser_sprite = pygame.image.load('sprites/projectiles/drone_projectile.png').convert_alpha()
projectile_dictionary['drone_laser'] = drone_laser_sprite


#Enemy Dictionary (animated and un-animated)
enemy_dictionary = {}
#['asteroid1'] is an asteroid sprite 70x70
#['asteroid2'] is a large asteroid sprite 140x140
#['exp_barrel1'] is an explosive barrel sprite 40x70
#['fighter1'] is a fighter ship 120x65
#['shielder1'] is a shielder ship 110x54
#['tracker1'] is a tracker ship 60x30

#Asteroids
asteroid_sprite1 = pygame.image.load('sprites/enemies/asteroid/asteroid_1.png').convert_alpha()
enemy_dictionary['asteroid1'] = asteroid_sprite1

asteroid_sprite2 = pygame.image.load('sprites/enemies/asteroid/asteroid_2.png').convert_alpha()
enemy_dictionary['asteroid2'] = asteroid_sprite2

#Explosive Barrel1
barrel_sprite1 = pygame.image.load('sprites/enemies/explosive_barrel/exp_barrel1.png').convert_alpha()
enemy_dictionary['exp_barrel1'] = barrel_sprite1

#Battleship drone
battleship_drone_sprite = pygame.image.load('sprites/enemies/battleship_drone/drone.png').convert_alpha()
enemy_dictionary['battleship_drone'] = battleship_drone_sprite

#fighter1
fighter1_sequence = []
fighter_sprite1 = pygame.image.load('sprites/enemies/fighters/fighter1.png').convert_alpha()
fighter1_sequence.append(fighter_sprite1)
fighter_sprite2 = pygame.image.load('sprites/enemies/fighters/fighter2.png').convert_alpha()
fighter1_sequence.append(fighter_sprite2)
fighter_sprite3 = pygame.image.load('sprites/enemies/fighters/fighter3.png').convert_alpha()
fighter1_sequence.append(fighter_sprite3)
fighter_sprite4 = pygame.image.load('sprites/enemies/fighters/fighter4.png').convert_alpha()
fighter1_sequence.append(fighter_sprite4)
enemy_dictionary['fighter1'] = fighter1_sequence


#shielder1
shielder1_sequence = []
shielder_sprite1 = pygame.image.load('sprites/enemies/shielder/shielder1.png').convert_alpha()
shielder1_sequence.append(shielder_sprite1)
shielder_sprite2 = pygame.image.load('sprites/enemies/shielder/shielder2.png').convert_alpha()
shielder1_sequence.append(shielder_sprite2)
shielder_sprite3 = pygame.image.load('sprites/enemies/shielder/shielder3.png').convert_alpha()
shielder1_sequence.append(shielder_sprite3)
shielder_sprite4 = pygame.image.load('sprites/enemies/shielder/shielder4.png').convert_alpha()
shielder1_sequence.append(shielder_sprite4)
enemy_dictionary['shielder1'] = shielder1_sequence


#tracker1
tracker1_sequence = []
tracker_sprite1 = pygame.image.load('sprites/enemies/tracker/tracker1.png').convert_alpha()
tracker1_sequence.append(tracker_sprite1)
tracker_sprite2 = pygame.image.load('sprites/enemies/tracker/tracker2.png').convert_alpha()
tracker1_sequence.append(tracker_sprite2)
tracker_sprite3 = pygame.image.load('sprites/enemies/tracker/tracker3.png').convert_alpha()
tracker1_sequence.append(tracker_sprite3)
tracker_sprite4 = pygame.image.load('sprites/enemies/tracker/tracker4.png').convert_alpha()
tracker1_sequence.append(tracker_sprite4)
enemy_dictionary['tracker1'] = tracker1_sequence

#evil eye sequence
evil_eye_sequence = []
frame1 = pygame.image.load('sprites/enemies/evil_eye/frame1.png').convert_alpha()
evil_eye_sequence.append(frame1)
frame2 = pygame.image.load('sprites/enemies/evil_eye/frame2.png').convert_alpha()
evil_eye_sequence.append(frame2)
frame3 = pygame.image.load('sprites/enemies/evil_eye/frame3.png').convert_alpha()
evil_eye_sequence.append(frame3)
frame4 = pygame.image.load('sprites/enemies/evil_eye/frame4.png').convert_alpha()
evil_eye_sequence.append(frame4)
enemy_dictionary['evil_eye1'] = evil_eye_sequence

#battleship sequence
battleship_sequence = []
frame1 = pygame.image.load('sprites/enemies/battleship_boss/frame1.png').convert_alpha()
battleship_sequence.append(frame1)
frame2 = pygame.image.load('sprites/enemies/battleship_boss/frame2.png').convert_alpha()
battleship_sequence.append(frame2)
frame3 = pygame.image.load('sprites/enemies/battleship_boss/frame3.png').convert_alpha()
battleship_sequence.append(frame3)
frame4 = pygame.image.load('sprites/enemies/battleship_boss/frame4.png').convert_alpha()
battleship_sequence.append(frame4)
enemy_dictionary['battleship'] = battleship_sequence


#MISC-------------------

health_pack_sprite = pygame.image.load('sprites/misc/health_pack.png').convert_alpha()

#PARTICLE EFFECTS---------------------------------------------------------------

#explosion sequence
explosion_sequence = []
frame1 = pygame.image.load('sprites/explosion_sequences/explosion/frame1.png').convert_alpha()
explosion_sequence.append(frame1)
frame2 = pygame.image.load('sprites/explosion_sequences/explosion/frame2.png').convert_alpha()
explosion_sequence.append(frame2)
frame3 = pygame.image.load('sprites/explosion_sequences/explosion/frame3.png').convert_alpha()
explosion_sequence.append(frame3)
frame4 = pygame.image.load('sprites/explosion_sequences/explosion/frame4.png').convert_alpha()
explosion_sequence.append(frame4)
frame5 = pygame.image.load('sprites/explosion_sequences/explosion/frame5.png').convert_alpha()
explosion_sequence.append(frame5)
frame6 = pygame.image.load('sprites/explosion_sequences/explosion/frame6.png').convert_alpha()
explosion_sequence.append(frame6)
frame7 = pygame.image.load('sprites/explosion_sequences/explosion/frame7.png').convert_alpha()
explosion_sequence.append(frame7)

#explosion sequence 2
explosion_sequence2 = []
frame1 = pygame.image.load('sprites/explosion_sequences/explosion2/frame1.png').convert_alpha()
explosion_sequence2.append(frame1)
frame2 = pygame.image.load('sprites/explosion_sequences/explosion2/frame2.png').convert_alpha()
explosion_sequence2.append(frame2)
frame3 = pygame.image.load('sprites/explosion_sequences/explosion2/frame3.png').convert_alpha()
explosion_sequence2.append(frame3)
frame4 = pygame.image.load('sprites/explosion_sequences/explosion2/frame4.png').convert_alpha()
explosion_sequence2.append(frame4)
frame5 = pygame.image.load('sprites/explosion_sequences/explosion2/frame5.png').convert_alpha()
explosion_sequence2.append(frame5)
frame6 = pygame.image.load('sprites/explosion_sequences/explosion2/frame6.png').convert_alpha()
explosion_sequence2.append(frame6)

#asteroid explosion sequence
asteroid_explosion_sequence = []
frame1 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame1.png').convert_alpha()
asteroid_explosion_sequence.append(frame1)
frame2 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame2.png').convert_alpha()
asteroid_explosion_sequence.append(frame2)
frame3 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame3.png').convert_alpha()
asteroid_explosion_sequence.append(frame3)
frame4 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame4.png').convert_alpha()
asteroid_explosion_sequence.append(frame4)
frame5 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame5.png').convert_alpha()
asteroid_explosion_sequence.append(frame5)
frame6 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame6.png').convert_alpha()
asteroid_explosion_sequence.append(frame6)
frame7 = pygame.image.load('sprites/explosion_sequences/asteroid_explosion/frame7.png').convert_alpha()
asteroid_explosion_sequence.append(frame7)

#impact explosion sequence
impact_explosion_sequence = []
frame1 = pygame.image.load('sprites/explosion_sequences/bullet_impact/frame1.png').convert_alpha()
impact_explosion_sequence.append(frame1)
frame2 = pygame.image.load('sprites/explosion_sequences/bullet_impact/frame2.png').convert_alpha()
impact_explosion_sequence.append(frame2)
frame3 = pygame.image.load('sprites/explosion_sequences/bullet_impact/frame3.png').convert_alpha()
impact_explosion_sequence.append(frame3)
frame4 = pygame.image.load('sprites/explosion_sequences/bullet_impact/frame4.png').convert_alpha()
impact_explosion_sequence.append(frame4)
frame5 = pygame.image.load('sprites/explosion_sequences/bullet_impact/frame5.png').convert_alpha()
impact_explosion_sequence.append(frame5)

#shield impact explosion sequence
shield_impact_sequence = []
frame1 = pygame.image.load('sprites/explosion_sequences/shield_impact/frame1.png').convert_alpha()
shield_impact_sequence.append(frame1)
frame2 = pygame.image.load('sprites/explosion_sequences/shield_impact/frame2.png').convert_alpha()
shield_impact_sequence.append(frame2)
frame3 = pygame.image.load('sprites/explosion_sequences/shield_impact/frame3.png').convert_alpha()
shield_impact_sequence.append(frame3)
frame4 = pygame.image.load('sprites/explosion_sequences/shield_impact/frame4.png').convert_alpha()
shield_impact_sequence.append(frame4)

#blood impact explosion sequence
blood_impact_sequence = []
frame1 = pygame.image.load('sprites/explosion_sequences/blood_explosion/frame1.png').convert_alpha()
blood_impact_sequence.append(frame1)
frame2 = pygame.image.load('sprites/explosion_sequences/blood_explosion/frame2.png').convert_alpha()
blood_impact_sequence.append(frame2)
frame3 = pygame.image.load('sprites/explosion_sequences/blood_explosion/frame3.png').convert_alpha()
blood_impact_sequence.append(frame3)
frame4 = pygame.image.load('sprites/explosion_sequences/blood_explosion/frame4.png').convert_alpha()
blood_impact_sequence.append(frame4)
