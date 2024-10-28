import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Vehicle:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def move(self):
        self.x += self.speed / FPS  # Adjust movement based on speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 30))

def parse_prompt(prompt):
    # A basic parser that can be expanded
    if "two-wheeler" in prompt:
        two_wheeler_speed = int(prompt.split("at ")[1].split(" km/h")[0])
        return Vehicle(100, HEIGHT // 2, (255, 0, 0), two_wheeler_speed)
    if "four-wheeler" in prompt:
        four_wheeler_speed = int(prompt.split("at ")[2].split(" km/h")[0])
        return Vehicle(600, HEIGHT // 2, (0, 0, 255), four_wheeler_speed)

def main(prompt):
    vehicle = parse_prompt(prompt)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Clear the screen
        vehicle.move()
        vehicle.draw()

        # Add collision detection and animation logic here
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    # Example prompt
    prompt = "On 4-lane divided national highways, a two-wheeler is traveling at 80 km/h and a four-wheeler at 120 km/h."
    main(prompt)
