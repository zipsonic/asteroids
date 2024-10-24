import random
import copy
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,WHITE,(int(self.position.x), int(self.position.y)),self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):

        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            split_angle = random.uniform(20,50)
            for i in range(0,2):
                asteroid = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
                if i == 1:
                    asteroid.velocity = self.velocity.rotate(split_angle) * 1.2

                else:
                    asteroid.velocity = self.velocity.rotate(split_angle * -1) * 1.2
        
        
            
