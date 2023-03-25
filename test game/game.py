import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Defender")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
player_speed = 5
bullet_speed = 10
enemy_speed = 3
score = 0
game_over = False

# Load the game images
player_image = pygame.image.load("player.png")
bullet_image = pygame.image.load("bullet.png")
enemy_image = pygame.image.load("enemy.png")

# Set up the game objects
player = player_image.get_rect(center=(width // 2, height - 50))
bullets = []
enemies = []

# Set up the game fonts
font = pygame.font.Font(None, 30)

# Set up the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_ip(-player_speed, 0)
            elif event.key == pygame.K_RIGHT:
                player.move_ip(player_speed, 0)
            elif event.key == pygame.K_SPACE:
                bullet = bullet_image.get_rect(center=player.center)
                bullets.append(bullet)

    # Move the bullets
    for bullet in bullets:
        bullet.move_ip(0, -bullet_speed)

    # Remove the bullets that go off the screen
    bullets = [bullet for bullet in bullets if bullet.top > 0]

    # Spawn enemies
    if random.randint(0, 100) < 2:
        enemy = enemy_image.get_rect(center=(random.randint(0, width), 0))
        enemies.append(enemy)

    # Move the enemies
    for enemy in enemies:
        enemy.move_ip(0, enemy_speed)

    # Remove the enemies that go off the screen
    enemies = [enemy for enemy in enemies if enemy.bottom < height]

    # Check for collisions between bullets and enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Draw the game objects
    window.fill((0, 0, 0))
    window.blit(player_image, player)
    for bullet in bullets:
        window.blit(bullet_image, bullet)
    for enemy in enemies:
        window.blit(enemy_image, enemy)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
