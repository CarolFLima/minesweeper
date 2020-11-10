import random

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        if difficulty == 'EASY':
            self.no_bombs = 10
            self.field_size = (9, 9)
        elif difficulty == 'MEDIUM':
            self.no_bombs = 40
            self.field_size = (16, 16)
        self.status = 0

    def generate_field(self):
        self.field = [[0 for row in range(self.field_size[0])] for column in range(self.field_size[1])]
        self.player_field = [['-' for row in range(self.field_size[0])] for column in range(self.field_size[1])]
        for _ in range(self.no_bombs):
            x = random.randint(0, self.field_size[0]-1)
            y = random.randint(0, self.field_size[1]-1)
            self.field[x][y] = 9

        for row in range(self.field_size[0]):
            for col in range(self.field_size[1]):
                if self.field[row][col] == 9:
                    continue
                
                #Upper cell
                if row > 0 and self.field[row-1][col] == 9:
                    self.field[row][col] += 1

                #Bottom cell
                if row < self.field_size[0]-1 and self.field[row+1][col] == 9:
                    self.field[row][col] += 1
                
                #Left cell
                if col > 0 and self.field[row][col-1] == 9:
                    self.field[row][col] += 1

                #Right cell
                if col < self.field_size[1]-1 and self.field[row][col+1] == 9:
                    self.field[row][col] += 1
                
                #Upper left corner cell
                if col > 0 and row > 0 and self.field[row-1][col-1] == 9:
                    self.field[row][col] += 1

                #Upper right corner cell
                if col < self.field_size[1]-1 and row > 0 and self.field[row-1][col+1] == 9:
                    self.field[row][col] += 1

                #Bottom left corner cell
                if col > 0 and row < self.field_size[0]-1 and self.field[row+1][col-1] == 9:
                    self.field[row][col] += 1

                #Bottom right corner cell
                if col < self.field_size[1]-1 and row < self.field_size[0]-1 and self.field[row+1][col+1] == 9:
                    self.field[row][col] += 1

    def dig(self, x_pos, y_pos):
        if self.field[x_pos][y_pos] == 0:
            self.dig_adjacent_zeros(x_pos, y_pos)
        elif self.field[x_pos][y_pos] != 9:
            self.player_field[x_pos][y_pos] = self.field[x_pos][y_pos]
        else:
            self.status = 1
            print('YOU\'VE HIT A BOMB')

    def dig_adjacent_zeros(self, x_pos, y_pos):
        if self.field[x_pos][y_pos] == 0:
            self.player_field[x_pos][y_pos] = 0
            
            if x_pos > 0 and self.field[x_pos-1][y_pos] == 0 and self.player_field[x_pos-1][y_pos] == '-':
                self.dig_adjacent_zeros(x_pos-1, y_pos)
            if y_pos < self.field_size[1]-1 and self.field[x_pos][y_pos+1] == 0 and self.player_field[x_pos][y_pos+1] == '-':
                self.dig_adjacent_zeros(x_pos, y_pos+1)
            if x_pos < self.field_size[0]-1 and self.field[x_pos+1][y_pos] == 0 and self.player_field[x_pos+1][y_pos] == '-':
                self.dig_adjacent_zeros(x_pos+1, y_pos)
            if y_pos > 0 and self.field[x_pos][y_pos-1] == 0 and self.player_field[x_pos][y_pos-1] == '-': 
                self.dig_adjacent_zeros(x_pos, y_pos-1)
            if x_pos > 0 and y_pos > 0 and self.field[x_pos-1][y_pos-1] == 0 and self.player_field[x_pos-1][y_pos-1] == '-':
                self.dig_adjacent_zeros(x_pos-1, y_pos-1)
            if x_pos > 0 and y_pos < self.field_size[1]-1 and self.field[x_pos-1][y_pos+1] == 0 and self.player_field[x_pos-1][y_pos+1] == '-':
                self.dig_adjacent_zeros(x_pos-1, y_pos+1)
            if x_pos < self.field_size[0]-1 and y_pos < self.field_size[1]-1 and self.field[x_pos+1][y_pos+1] == 0 and self.player_field[x_pos+1][y_pos+1] == '-':
                self.dig_adjacent_zeros(x_pos+1, y_pos+1)
            if x_pos < self.field_size[0]-1 and y_pos > 0 and self.field[x_pos+1][y_pos-1] == 0 and self.player_field[x_pos+1][y_pos-1] == '-':
                self.dig_adjacent_zeros(x_pos+1, y_pos-1)

    def solver(self):
        pass

    def print_field(self):
        for row in self.player_field:
            print(" ".join(str(cell) for cell in row))
            

game = Game('EASY')
game.generate_field()
game.print_field()

while game.status == 0:
    x, y = map(int, input().split())
    game.dig(x, y)
    game.print_field()
    