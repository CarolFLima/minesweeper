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

    def generate_field(self):
        self.field = [[0 for row in range(self.field_size[0])] for column in range(self.field_size[1])]
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


    def print_field(self):
        for row in self.field:
            print(" ".join(str(cell) for cell in row))


game = Game('EASY')
game.generate_field()
game.print_field()
