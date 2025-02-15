import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Define the linear interpolation function for moving a Rect
def lerp_move_rect(rect, target_rect, total_time, start_time):
    """
    Linearly interpolate the position of the given rect towards the target_rect.
    
    rect: The rect to move (pygame.Rect).
    target_rect: The destination rect (pygame.Rect).
    total_time: The total time (in seconds) to move from rect to target_rect.
    start_time: The time (in seconds) when the movement started.
    
    Updates rect's position and returns it.
    """
    # Calculate elapsed time (in seconds)
    elapsed_time = (pygame.time.get_ticks() / 1000) - start_time
    
    # Ensure elapsed_time doesn't exceed total_time
    t = min(elapsed_time / total_time, 1)
    
    # Interpolate x and y coordinates separately
    rect.x = rect.x + (target_rect.x - rect.x) * t
    rect.y = rect.y + (target_rect.y - rect.y) * t
    
    # Return the updated rect with the interpolated position
    return rect, elapsed_time

# Initial positions (as pygame.Rect objects)
rect = pygame.Rect(100, 100, 50, 50)  # Starting position
target_rect = pygame.Rect(700, 500, 50, 50)  # Target position

# Time to move from rect to target_rect in seconds
total_time = 3  # 3 seconds to move

# Set up variables for timing
start_time = 0  # Start time will be set when key is pressed
moving = False  # To track whether the rectangle is moving

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Check for events (key press and key release)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Start moving when the SPACE key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not moving:
                moving = True  # Start movement
                start_time = pygame.time.get_ticks() / 1000  # Set start time when key is pressed

    
    # Only move the rect if we're in the "moving" state
    if moving:
        rect, elapsed_time = lerp_move_rect(rect, target_rect, total_time, start_time)

        # Ensure movement stops after the total time has passed
        if elapsed_time >= total_time:
            moving = False

    # Draw the rect (a red square)
    pygame.draw.rect(screen, (255, 0, 0), rect)

    # Update the display
    pygame.display.flip()

    # Frame rate (in frames per second)
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
