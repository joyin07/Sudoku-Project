import pygame, sys
class Board():
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
            print((((self.width-12)//3)*j+buff, 0),
                (((self.width-12)//3)*j+buff, self.height-40))
            # draw horizontal lines
            pygame.draw.line(
                self.screen,
                line_color,
                (0, ((self.height-52)//3)*j+buff),
                (self.width, ((self.height-52)//3)*j+buff),
                6)
            print((0, ((self.height-52)//3)*j+buff),
                (self.width, ((self.height-52)//3)*j+buff))
            buff += 6

        # length of individual cell is 196
        # START HERE
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
                print((buffer+(64 * mini_line + (buff_2*(mini_line-1))), 0),
                    (buffer+(64 * mini_line + (buff_2*(mini_line-1))), self.height - 40))
                # mini horizontal lines
                pygame.draw.line(
                    self.screen,
                    line_color,
                    (0, buffer+(64 * mini_line + (buff_2*(mini_line-1)))),
                    (self.width, buffer+(64 * mini_line + (buff_2*(mini_line-1)))),
                    2)
                print((0, buffer+(64 * mini_line + (buff_2*(mini_line-1)))),
                    (self.width, buffer+(64 * mini_line + (buff_2*(mini_line-1)))))
            buffer += 202
        pygame.draw.line(
            self.screen,
            line_color,
            (0, 404 + (64 * 3 + (2 * (3 - 1)))),
            (self.width, 404 + (64 * 3 + (2 * (3 - 1)))),
            2)

    def select(self, row, col):
        pass
    def click(self, x, y):
        pass
    def clear(self):
        pass
    def sketch(self, value):
        pass
    def place_number(self, value):
        pass
    def reset_to_original(self):
        pass
    def is_full(self):
        pass
    def update_board(self):
        pass
    def check_board(self):
        pass
