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
    game.flag_bomb(pos_x, pos_y)

def solver():
    print('solving...')
    reveal_cell([60, 60])
    counter = 0
    y_pos = 0
    while counter < 300:
        x_pos = ((counter//7)%7) + 1
        y_pos = (counter%7) + 1
        if game.player_field[x_pos][y_pos]>0 and game.player_field[x_pos][y_pos]<10: 
            flagged_bombs, hidden_cells = inspect_neighbors(x_pos, y_pos)
            if hidden_cells+flagged_bombs == game.player_field[x_pos][y_pos]:
                flag_neighbors(x_pos, y_pos)
            if flagged_bombs == game.player_field[x_pos][y_pos]:
                reveal_neighbors(x_pos, y_pos)
        counter += 1 
        pygame.display.update() 
        pygame.time.delay(20)
        
def inspect_neighbors(x_pos, y_pos):
    hidden_cells = 0
    flagged_bombs = 0
    for row in game.player_field[x_pos-1:x_pos+2]:
        hidden_cells += row[y_pos-1:y_pos+2].count(-1)
        flagged_bombs += row[y_pos-1:y_pos+2].count(10)
    return flagged_bombs, hidden_cells    

def flag_neighbors(x_pos, y_pos):
    for row in range(x_pos-1, x_pos+2):
        for col in range(y_pos-1, y_pos+2):
            if game.player_field[row][col]==-1:
                flag_bomb([row*50, col*50])

def reveal_neighbors(x_pos, y_pos):
    for row in range(x_pos-1, x_pos+2):
        for col in range(y_pos-1, y_pos+2):
            if game.player_field[row][col]<0:
                reveal_cell([row*50, col*50])

run = True
draw_field()
debounce_flag = 0
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
    elif event.type == pygame.KEYUP and debounce_flag == 0:
        if event.key == pygame.K_SPACE:
            debounce_flag = 1
            solver()
            run = True

    pygame.display.update() 
    pygame.time.delay(50)

# pygame.quit()