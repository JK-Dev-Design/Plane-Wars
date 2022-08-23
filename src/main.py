import pygame
import entity
import bullet

pygame.init()
screen = pygame.display.set_mode((800, 800))
playerimg = pygame.image.load("src/Player.png")
blackimg = pygame.image.load("src/BlackPlane.png")
greenimg = pygame.image.load("src/GreenPlane.png")
entity = entity.entity(pygame.Vector2(0, 700), 5, 10, 1, playerimg)
pygame.display.set_caption("Plane Wars")
moving_left = False
moving_right = False
bullets = []
def fire():
  global bullets

  b = bullet.bullet(entity.position.copy(), 1, 8, 1, blackimg, velocity=pygame.Vector2(0, -10))
  bullets.append(b)
while True:
  ev = pygame.event.get()
  for event in ev:
    if event.type == pygame.KEYDOWN:
      if pygame.K_LEFT == event.key:
        moving_left = True
      if pygame.K_RIGHT == event.key:
        moving_right = True
    if event.type == pygame.KEYUP:
      if pygame.K_LEFT == event.key:
        moving_left = False
      if pygame.K_RIGHT == event.key:
        moving_right = False
      if pygame.K_SPACE == event.key:
        fire()
    if event.type == pygame.QUIT:
      pygame.quit()
  if moving_left == True:
    entity.position.x -= entity.speed #TypeError: unsupported operand type(s) for -=: 'float' and 'pygame.math.Vector2'
  if moving_right == True:
    entity.position.x += entity.speed
    
  screen.fill((255, 255, 255))
  entity.draw(screen)
  for i in bullets:
    i.draw(screen)
    i.update()
  pygame.display.flip()
