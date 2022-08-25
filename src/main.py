import pygame
import entity
import bullet
import clock
import random
import copy

pygame.init()
screen = pygame.display.set_mode((800, 800))
playerimg = pygame.image.load("src/Player.png")
# playerimg = pygame.transform.scale(
#       playerimg, pygame.Vector2(playerimg.get_size()) / 6)
blackimg = pygame.image.load("src/BlackPlane.png")
greenimg = pygame.image.load("src/GreenPlane.png")
pbulletimg = pygame.image.load("src/P_Bullet_Rect.png")
targetimg_2 = pygame.image.load("src/peppa_pig.png")
targetimg_2 = pygame.transform.scale(
      targetimg_2, pygame.Vector2(targetimg_2.get_size()) / 7)
targetimg = pygame.image.load("src/george.jpg")
targetimg = pygame.transform.scale(
      targetimg, pygame.Vector2(targetimg.get_size()) / 7)
player_entity = entity.entity(pygame.Vector2(0, 700), 5, 10, 1, playerimg)
peppa_entity = entity.entity(pygame.Vector2(0, 700), 5, 10, 1, targetimg_2)
george_entity = entity.entity(pygame.Vector2(0, 700), 5, 10, 1, targetimg)
bullet_clock = clock.clock()
enemy_clock = clock.clock()
pygame.display.set_caption("Plane Wars")
moving_left = False
moving_right = False
space_pressed = False
bullets = []
enemies = []
def fire():
  if bullet_clock.time_passed() >= 0.3:
    global bullets
    bullet_size = pygame.Vector2(playerimg.get_size()) / 2
    b = bullet.bullet(player_entity.position.copy() + bullet_size, 1, 8, 1, pbulletimg, velocity = pygame.Vector2(0, -10))
    b.velocity = pygame.Vector2(0, -10)
    bullets.append(b)
    bullet_clock.reset()

def spawn_enemies(amount):
  for b in range(amount):
    enemy = george_entity.copy()
    enemy.position = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, 10))
    enemy.velocity = pygame.Vector2(0, 7)
    enemy2 = peppa_entity.copy()
    enemy2.position = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, 10))
    enemy2.velocity = pygame.Vector2(0, 5)
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
  for i in enemies:
    i.draw(screen)
    i.update()
  player_entity.draw(screen)
  for i in bullets:
    i.draw(screen)
    i.update()
  pygame.display.flip()
