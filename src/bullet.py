import pygame
import math

class bullet:
    def __init__(self, position, damage, speed, type, size, color, velocity=pygame.Vector2(0, 5)):
      self.position = position
      self.damage = damage
      self.speed = speed
      self.type = type
      self.size = size
      self.color = color
      self.velocity = velocity
      self.rect = pygame.Rect(position, size)
    def update(self):
      self.position = self.velocity+self.position
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    def calcvelocity(self, degrees, speed):
        self.degrees = degrees
        self.velocity.x = math.sin(math.radians(degrees)) * speed
        self.velocity.y = math.cos(math.radians(degrees)) * speed