import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

fps = pygame.time.Clock()

x_pos = background.get_size()[0]//2 #240
y_pos = background.get_size()[1]//2 #180

to_x = 0
to_y = 0

play = True
while play:
    delattime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                 to_y = -10
            elif event.key==pygame.K_DOWN:
                 to_y = 10
            elif event.key==pygame.K_RIGHT:
                 to_x = 10
            elif event.key==pygame.K_LEFT:
                 to_x = -10
        if event.type == pygame.KEYUP:
            to_x = 0
            to_y = 0
             # if event.key==pygame.K_UP:
             #    to_y = 0
             # elif event.key==pygame.K_DOWN:
             #    to_y = 0
             # elif event.key==pygame.K_RIGHT:
             #    to_x = 0
             # elif event.key==pygame.K_LEFT:
             #    to_x = 0

        x_pos += to_x
        y_pos += to_y

        background.fill((255,0,0))
        pygame.draw.circle(background, (0,0,255), (x_pos,y_pos), 5)
        pygame.display.update()

pygame.quit()

        