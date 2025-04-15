import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print('Game Over!')
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("BLACK")
        for drawable in drawables:
            drawable.draw(screen) 
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000  # convert milliseconds to seconds
    
if __name__ == "__main__":
    main()