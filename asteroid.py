import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    rand_angle = random.uniform(20, 50)
    vel1 = self.velocity.rotate(-rand_angle)
    vel2 = self.velocity.rotate(rand_angle)
    radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid1 = Asteroid(self.position.x, self.position.y, radius)
    asteroid1.velocity = vel1 * 1.2
    asteroid2 = Asteroid(self.position.x, self.position.y, radius)
    asteroid2.velocity = vel2 * 1.2