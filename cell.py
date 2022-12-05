import pygame
from sudoku import *
class Cell:
    # initialize values for Cell
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    # displays intended cell value
    def set_cell_value(self, value):
        num_color = (43, 45, 47) # dark gray
        num_font = pygame.font.Font(None, 50)
        num_surface = num_font.render(f"{self.value}", 1, num_color)
        num_rectangle = num_surface.get_rect(
            center=(self.col * 66 + 35, self.row * 66 + 38))
        self.screen.blit(num_surface, num_rectangle)

    # displays the user sketch value
    def set_sketched_value(self, grid):
        if grid[self.row][self.col] == 0 and self.value != 0:
            pygame.draw.rect(self.screen, (255, 255, 245),
                             pygame.Rect(self.col*66 +20, self.row*66 +20, 32, 32))
            pygame.display.flip()
            num_color = (135, 206, 235)  # light blue
            num_font = pygame.font.Font(None, 50)
            num_surface = num_font.render(f"{self.value}", 1, num_color)
            num_rectangle = num_surface.get_rect(
                center=(self.col*66 + 35, self.row * 66 + 38))
            self.screen.blit(num_surface, num_rectangle)
            return True
        else:
            return False
    # displays the final or entered number
    def set_final_value(self, sketched_value_grid):
        if sketched_value_grid[self.row][self.col] != 0:
            pygame.draw.rect(self.screen, (255, 255, 245),
                             pygame.Rect(self.col * 66 + 20, self.row * 66 + 20, 32, 32))
            pygame.display.flip()
            num_color = (250, 70, 22) # orange
            num_font = pygame.font.Font(None, 50)
            num_surface = num_font.render(f"{sketched_value_grid[self.row][self.col]}", 1, num_color)
            num_rectangle = num_surface.get_rect(
                center=(self.col*66 + 35, self.row * 66 + 38))
            self.screen.blit(num_surface, num_rectangle)
        else:
            return False
    # draws the red outline with correct spacing
    def draw_border(self, row, col, color):
        if col in [0, 1, 2]:
            if row in [0, 1, 2]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66, self.row * 65 + (self.row-2), 64, 66), 2)
            elif row in [3, 4, 5]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66, self.row * 65 + (self.row-2) + 4, 64, 66), 2)
            elif row in [6, 7, 8]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66, self.row * 65 + (self.row-2) + 8, 64, 66), 2)
        elif col in [3, 4, 5]:
            if row in [0, 1, 2]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66 + 2, self.row * 65 + (self.row-2), 66, 66), 2)
            elif row in [3, 4, 5]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66 + 2, self.row * 65 + (self.row-2) + 4, 66, 66), 2)
            elif row in [6, 7, 8]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66 + 2, self.row * 65 + (self.row-2) + 8, 66, 66), 2)
        elif col in [6, 7, 8]:
            if row in [0, 1, 2]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66 + 6, self.row * 65 + (self.row-2), 66, 66), 2)
            elif row in [3, 4, 5]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66 + 6, self.row * 65 + (self.row-2) + 4, 66, 66), 2)
            elif row in [6, 7, 8]:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(self.col * 66 + 6, self.row * 65 + (self.row-2) + 8, 66, 66), 2)
        pygame.display.update()
    # to draw the cell value or return True
    def draw(self):
        if self.value != 0:
            self.set_cell_value(self.value)
        else:
            return True