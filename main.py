import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)

        for obj in asteroids:
            for shot in shots:
                if shot.collision_check(obj):
                    obj.kill()
            if obj.collision_check(player):
                print("Game Over!")
                running = False
                
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000

if __name__ == "__main__":
    main()