import pygame, sys
class Board():
    # initialize the values for Board
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    # draws the entire Sudoku grid
    def draw(self):
        screen_color = (255, 255, 245)
        self.screen.fill(screen_color)
        line_color = (0, 33, 165)
        buff = 0
        for j in range(1, 3):
            # draw vertical lines
            pygame.draw.line(
                self.screen,
                line_color,
                (((self.width-12)//3)*j+buff, 0),
                (((self.width-12)//3)*j+buff, self.height-40),
                6)
            # draw horizontal lines
            pygame.draw.line(
                self.screen,
                line_color,
                (0, ((self.height-52)//3)*j+buff),
                (self.width, ((self.height-52)//3)*j+buff),
                6)
            buff += 6

        # length of individual cell is 196
        buffer = 0
        for iter in range(3):
            buff_2 = 2
            for mini_line in range(1, 3):
                # mini vertical lines
                pygame.draw.line(
                    self.screen,
                    line_color,
                    (buffer+(64 * mini_line + (buff_2*(mini_line-1))), 0),
                    (buffer+(64 * mini_line + (buff_2*(mini_line-1))), self.height - 40),
                    2)
                # mini horizontal lines
                pygame.draw.line(
                    self.screen,
                    line_color,
                    (0, buffer+(64 * mini_line + (buff_2*(mini_line-1)))),
                    (self.width, buffer+(64 * mini_line + (buff_2*(mini_line-1)))),
                    2)
            buffer += 202
        pygame.draw.line(
            self.screen,
            line_color,
            (0, 404 + (64 * 3 + (2 * (3 - 1)))),
            (self.width, 404 + (64 * 3 + (2 * (3 - 1)))),
            2)
    # to check if the correct value is on board
    def check_board(self, row, col, grid):
        if self.valid_in_box(row - (row % 3), col - (col % 3), grid):
            if self.valid_in_row(row, grid):
                if self.valid_in_col(col, grid):
                    return True
        return False
    # to check if value is repeated in row
    def valid_in_row(self, row, grid):
        memory = []
        for i in grid[row]:
            if i not in memory:
                memory.append(i)
            else:
                return False
        return True

    # to check if value is repeated in col
    def valid_in_col(self, col, grid):
        memory = []
        for row in grid:
            for index, num_cols in enumerate(row):
                if index == col:
                    if num_cols not in memory:
                        memory.append(num_cols)
                    else:
                        return False
        return True

    # to check if value is repeated in 3X3 box
    def valid_in_box(self, row_start, col_start, grid):
        memory = []
        for row in range(3):
            for col in range(3):
                if grid[row_start + row][col_start + col] not in memory:
                    memory.append(grid[row_start + row][col_start + col])
                else:
                    print("box")
                    return False
        return True
