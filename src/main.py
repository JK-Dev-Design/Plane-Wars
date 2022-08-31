import pygame
import entity
import bullet
import clock
import random
import copy
import sys

quit = False

pygame.init()
score = 0
current_world = "main_world"
coins_collected = 0
collect_random = 0
font_name = "arial"
font = pygame.font.SysFont(font_name, 20)
screen = pygame.display.set_mode((800, 800))
playerimg = pygame.image.load("src/Player.png")
blackimg = pygame.image.load("src/BlackPlane.png")
greenimg = pygame.image.load("src/GreenPlane.png")
coinimg = pygame.image.load("src/Coin.png")
shieldimg = pygame.image.load("src/Shield.png")
shield_boost = pygame.image.load("src/Shield_Boost.png")
shield_re = pygame.image.load("src/Shield_Re.png")
heartimg = pygame.image.load("src/Heart.png")
pbulletimg = pygame.image.load("src/P_Bullet_Rect.png")
targetimg_2 = pygame.image.load("src/peppa_pig.png")
targetimg_2 = pygame.transform.scale(
      targetimg_2, pygame.Vector2(targetimg_2.get_size()) / 7)
targetimg = pygame.image.load("src/george.jpg")
targetimg = pygame.transform.scale(
      targetimg, pygame.Vector2(targetimg.get_size()) / 7)
player_entity = entity.entity(pygame.Vector2(0, 700), 5, 5, 1, playerimg)
peppa_entity = entity.entity(pygame.Vector2(0, 700), 5, 2, 1, targetimg_2)
george_entity = entity.entity(pygame.Vector2(0, 700), 5, 5, 1, targetimg)
collect_entity = entity.entity(pygame.Vector2(0, 0), 4, 0, 0, heartimg, velocity = pygame.Vector2(0, 1))
bullet_clock = clock.clock()
enemy_clock = clock.clock()
pygame.display.set_caption("Plane Wars")
moving_left = False
moving_right = False
space_pressed = False
bullets = []
enemies = []
coins = []
bullet_offsetx = [[0], [6, -6]]
current_upgrade = 1
def fire():
  if bullet_clock.time_passed() >= 0.1:
    global bullets
    bullet_size = pygame.Vector2(playerimg.get_size()) / 2
    global b
    offsets = bullet_offsetx[current_upgrade - 1]
    for i in offsets:      
      b = bullet.bullet(player_entity.position.copy() + bullet_size + pygame.Vector2(i, 0), 1, 8, 1, pbulletimg, velocity = pygame.Vector2(0, -10))
      b.velocity = pygame.Vector2(0, -10)
      bullets.append(b)
      bullet_clock.reset()

def spawn_enemies(amount):
  for b in range(amount):
    enemy = george_entity.copy()
    enemy.position = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, 10))
    enemy.velocity = pygame.Vector2(0, 1)
    enemy2 = peppa_entity.copy()
    enemy2.position = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, 10))
    enemy2.velocity = pygame.Vector2(0, 1)
    enemies.append(enemy)
    enemies.append(enemy2)

  
while True:
  ev = pygame.event.get()
  for event in ev:
    if event.type == pygame.KEYDOWN:
      if pygame.K_LEFT == event.key:
        moving_left = True
      if pygame.K_RIGHT == event.key:
        moving_right = True
      if pygame.K_SPACE == event.key:
        space_pressed = True
    if event.type == pygame.KEYUP:
      if pygame.K_LEFT == event.key:
        moving_left = False
      if pygame.K_RIGHT == event.key:
        moving_right = False
      if pygame.K_SPACE == event.key:
        space_pressed = False
    if event.type == pygame.QUIT:
      pygame.quit()
  if moving_left == True:
    player_entity.position.x -= player_entity.speed
  if moving_right == True:
    player_entity.position.x += player_entity.speed
  if space_pressed == True:
    fire()
  if enemy_clock.time_passed() >= 3:
    spawn_enemies(1)
    enemy_clock.reset()

  screen.fill((255, 255, 255))
  score_surface = font.render(str(score), True, (0, 0, 0))
  screen.blit(score_surface, (20, 20))
  coins_collected_surface = font.render(str(coins_collected), True, (0, 0, 0))
  screen.blit(coins_collected_surface, (20, 40))
  for i in enemies:
    i.draw(screen)
    i.update()
    if i.rect.colliderect(player_entity.rect):
      player_entity.health -= 1
    
  player_entity.draw(screen)
  for i in bullets:
    i.draw(screen)
    i.update()
    for e in enemies:
      i.collide(e.rect)
      if i.rect.colliderect(e.rect) == True:
        e.health -= i.damage
        if e.health <= 0:
          enemies.remove(e)
          score+=1
          c = collect_entity.copy()
          collect_random = random.randint(3, 7)
          c.position = e.position.copy()    
          if collect_random != 0:
              c.position = e.position.copy()   
              if collect_random == 1 or 2 or 3:
                print(collect_random)
                c.image = coinimg
              if collect_random == 4:
                c.image = heartimg
                print("yo")
              if collect_random == 5:
                c.image = shieldimg
              if collect_random == 6:
                c.image = shield_boost
              if collect_random == 7:
                c.image = shield_re
              coins.append(c)
            
  for i in coins:
    i.draw(screen)
    i.update()
    if i.rect.colliderect(player_entity.rect):
      coins.remove(i)
      coins_collected += 1
  if coins_collected >= 3 and current_upgrade < 2:
    coins_collected = 0
    current_upgrade += 1
  pygame.display.flip()