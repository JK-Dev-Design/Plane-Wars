import pygame
class entity:
  def __init__(self, position, speed, health, type, image):
    self.position = position
    self.speed = speed
    self.health = health
    self.type = type
    self.image = image
  def draw(self, surface):
    surface.blit(self.image, self.position)
  def update(self):
    pass