import pygame
import minesweeper as ms

pygame.init() 
pygame.font.init()
screen = pygame.display.set_mode((450, 450)) 
pygame.display.set_caption('Minesweeper')

game = ms.Game('EASY')

dif = 50
font1 = pygame.font.SysFont("comicsans", 40)

LEFT = 1
RIGHT = 3

def draw_field(): 
    screen.fill((0, 0, 0)) 

    for i in range (9): 
        for j in range (9): 
            pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif - 1, dif - 1)) 

def reveal_cell(pos):
    pos_x = pos[0]//50
    pos_y = pos[1]//50
    game.dig(pos_x, pos_y)

    for pos in game.revealed_values:
        pygame.draw.rect(screen, (211, 211, 211), (pos[0]*50, pos[1]*50, dif - 1, dif - 1)) 
        val = game.player_field[pos[0]][pos[1]]
        if val != 0:
            text1 = font1.render(str(val), 1, (0, 0, 0)) 
            screen.blit(text1, (pos[0]*50 + 17, pos[1]*50 + 12))

def flag_bomb(pos):
    pos_x = pos[0]//50
    pos_y = pos[1]//50
    pygame.draw.rect(screen, (211, 0, 0), (pos_x*50, pos_y*50, dif - 1, dif - 1)) 

run = True
draw_field()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        pos = pygame.mouse.get_pos()
        reveal_cell(pos)
    if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
        pos = pygame.mouse.get_pos()
        flag_bomb(pos)

    pygame.display.update() 
    pygame.time.delay(50)

pygame.quit()