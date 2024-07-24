import pygame
import sys
pygame.init()

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up the display
screen = pygame.display.set_mode((screen_width*0.95, screen_height*0.95))

# Main loop
running = True #I set it to true 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
