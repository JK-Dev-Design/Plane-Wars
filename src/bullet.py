import pygame
import math
import entity

class bullet(entity.entity):
    def __init__(self, position, damage, speed, type, image, velocity=pygame.Vector2(0, 5,)):
      self.damage = damage
      self.velocity = velocity
      super().__init__(position, speed, 0, type, image)
    def update(self):
      self.position = self.velocity+self.position
    def calcvelocity(self, degrees, speed):
        self.degrees = degrees
        self.velocity.x = math.sin(math.radians(degrees)) * speed
        self.velocity.y = math.cos(math.radians(degrees)) * speed