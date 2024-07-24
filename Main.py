import pygame
import sys
pygame.init()

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w*0.95
screen_height = screen_info.current_h*0.95


# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))

#get centre of canvas
canvas_centre_x = screen_width/2
canvas_centre_y = screen_height/2

lvl_boxes = [
    pygame.Rect(50, 50, 100, 100),
    pygame.Rect(200, 50, 100, 100),
    pygame.Rect(350, 50, 100, 100),
    pygame.Rect(500, 50, 100, 100),
    pygame.Rect(650, 50, 100, 100),
]


# Main loop
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION: #obtain the coords
            mouse_pos = pygame.mouse.get_pos()
            print(f"Mouse coordinates: {mouse_pos}")

    screen.fill((173, 165, 160)) #set the bacground to grey
    pygame.draw.rect(screen, (255, 0, 0), lvl_boxes)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
