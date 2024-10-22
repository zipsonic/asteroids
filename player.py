from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def draw(self,screen):
        pygame.draw.polygon(screen,WHITE,self.triangle(),2)
        
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED*dt)

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
            # ?
        if keys[pygame.K_d]:
            self.rotate(-abs(dt))
            # ?
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-abs(dt))

        if keys[pygame.K_LEFT]:
            self.rotate(dt)
            # ?
        if keys[pygame.K_RIGHT]:
            self.rotate(-abs(dt))
            # ?
        if keys[pygame.K_UP]:
            self.move(dt)
        
        if keys[pygame.K_DOWN]:
            self.move(-abs(dt))

        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()
                self.shot_timer = PLAYER_SHOOT_COOLDOWN   

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt