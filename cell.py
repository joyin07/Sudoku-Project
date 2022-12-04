import pygame
from sudoku import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        num_color = (43, 45, 47) # dark gray
        num_font = pygame.font.Font(None, 50)
        num_surface = num_font.render(f"{self.value}", 1, num_color)
        num_rectangle = num_surface.get_rect(
            center=(self.col * 66 + 35, self.row * 66 + 38))
        self.screen.blit(num_surface, num_rectangle)

    def set_sketched_value(self, value):
        if value[self.row][self.col] == 0:
            # 255, 255, 245
            #pygame.draw.rect(self.screen, (250, 70, 22),
                             #pygame.Rect(self.col*66, self.col*66 + 10, self.row*66, self.row * 66 + 100))
            #pygame.display.flip()
            num_color = (135, 206, 235)  # light blue
            num_font = pygame.font.Font(None, 50)
            num_surface = num_font.render(f"{self.value}", 1, num_color)
            num_rectangle = num_surface.get_rect(
                center=(self.col*66 + 10, self.row * 66 + 20))
            self.screen.blit(num_surface, num_rectangle)
            return True
        else:
            return False
    def set_final_value(self, value):
        if value[self.row][self.col]== 0:
            num_color = (250, 70, 22) # orange
            num_font = pygame.font.Font(None, 50)
            num_surface = num_font.render(f"{self.value}", 1, num_color)
            num_rectangle = num_surface.get_rect(
                center=(self.col*66 + 35, self.row * 66 + 38))
            self.screen.blit(num_surface, num_rectangle)
        else:
            return False

    def draw(self):
        if self.value != 0:
            self.set_cell_value(self.value)
        else:
            return True