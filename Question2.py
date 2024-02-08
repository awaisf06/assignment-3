import random
import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Side Scroller')

def menu():
    image = pygame.image.load('assets/menu.png')
    image = pygame.transform.scale(image, (640, 480))
    while True:
        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(200, 228):
                    game()

def game():
    pygame.font.init()
    image = pygame.image.load('assets/level1.png')
    image = pygame.transform.scale(image, (640, 480))
    bgx = 0

    player = pygame.image.load('assets/boy.png')
    player = pygame.transform.rotozoom(player, 0, 0.2)
    player_y = 325
    gravity = 1
    jumpcount = 0
    jump = 0

    crate = pygame.image.load('assets/crate.png')
    crate = pygame.transform.rotozoom(crate, 0, 0.8)
    crate_x = 700
    crate_speed = 2

    # Initialize score
    score = 0

    while True:
        screen.blit(image, (bgx - 640, 0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx + 640, 0))

        bgx = bgx - 1
        if bgx <= -640:
            bgx = 0

        p_rect = screen.blit(player, (50, player_y))
        if player_y < 325:
            player_y += gravity

        if jump == 1:
            player_y = player_y - 4
            jumpcount += 1
            if jumpcount > 40:
                jumpcount = 0
                jump = 0

        c_rect = screen.blit(crate, (crate_x, 360))
        crate_x -= crate_speed
        if crate_x < -50:
            crate_x = random.randint(700, 800)
            crate_speed = random.randint(2, 5)

        # Check for collision
        if p_rect.colliderect(c_rect):
            return

        # Display the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render("Score: {}".format(int(score)), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Increment the score (you can adjust this based on your game logic)
        score += 0.08

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                jump = 1

menu()
