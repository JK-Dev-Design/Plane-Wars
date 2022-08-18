import pygame
import entity
import bullet

pygame.init()
screen = pygame.display.set_mode((700, 700))
entity = entity.entity(pygame.Vector2(250, 250), 2,pygame.Vector2(5), 1, pygame.Vector2(50, 50),(0, 0, 255))
bullet = bullet.bullet(pygame.Vector2(100, 100), 10, 5, 1,pygame.Vector2(2, 6), (255, 0, 0))
pygame.display.set_caption("Plane Wars")
moving_left = False
moving_right = False
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
  if moving_left == True:
    entity.position.x -= entity.speed #TypeError: unsupported operand type(s) for -=: 'float' and 'pygame.math.Vector2'
  if moving_right == True:
    entity.position.x += entity.speed
  screen.fill((255, 255, 255))
  entity.draw(screen)
  bullet.draw(screen)