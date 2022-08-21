import pygame
class entity:
  def __init__(self, position, speed, health, type, size, color):
    self.position = position
    self.speed = speed
    self.health = health
    self.type = type
    self.size = size
    self.color = color
    self.rect = pygame.Rect(position, size)
  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)
