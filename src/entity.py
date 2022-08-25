import pygame
class entity:
  def __init__(self, position, speed, health, type, image, velocity=pygame.Vector2(0, 0),):
    self.position = position
    self.speed = speed
    self.health = health
    self.type = type
    self.image = image
    self.velocity = velocity
    self.rect = pygame.Rect(self.position, self.image.get_size())
  def draw(self, surface):
    surface.blit(self.image, self.position)
  def update(self):
    self.position = self.position + self.velocity
  def copy(self):
    return entity(self.position, self.speed, self.health, self.type, self.image)