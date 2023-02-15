import pygame, sys,random

# general setup

pygame.init()
clock = pygame.time.Clock()

def ball_anim():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
           ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        #ball_speed_y *= -1
def player_anim():
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height
def opponent_anim():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, - 1))
    ball_speed_x *= random.choice((1, -1))

# setuping up the window

screen_width = 860
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PONG')

# Game rectangles

ball = pygame.Rect(screen_width/2 - 8, screen_height/2 - 8, 16, 16)
player = pygame.Rect(screen_width - 20, screen_height/2 - 65, 10, 130)
opponent = pygame.Rect(10, screen_height/2 - 65, 10, 130)
light_grey = (200,200,200)

#Ball
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 6
player_speed = 0
opponent_speed = 7


# game loop
while True:
     for event in pygame.event.get():  # handleing input
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
                 player_speed += 7
             if event.key == pygame.K_UP:
                 player_speed -= 7

         if event.type == pygame.KEYUP:
             if event.key == pygame.K_DOWN:
                 player_speed -= 7
             if event.key == pygame.K_UP:
                 player_speed += 7
     ball_anim()
     player_anim()
     opponent_anim()

    # visuals
     screen.fill(pygame.Color('grey12'))
     pygame.draw.rect(screen,light_grey, player)
     pygame.draw.rect(screen, light_grey, opponent)
     pygame.draw.ellipse(screen, light_grey, ball)
     pygame.draw.aaline(screen, light_grey, (screen_width/ 2, 0), (screen_width/2, screen_height))

     # updating the window
     pygame.display.flip()
     clock.tick(60)

    