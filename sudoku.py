import pygame, sys
from Board import *
from sudoku_generator import *
from cell import *
import sudoku_generator
def draw_game_start(screen):
    screen_color = (255, 255, 245)
    screen.fill(screen_color)

    title_color = (0, 33, 165)      # blue
    button_color = (250, 70, 22)    # orange

    start_title_font = pygame.font.Font(None, 70)
    gm_font = pygame.font.Font(None, 60)
    button_font = pygame.font.Font(None, 40)

    # to display title mode
    title_surface = start_title_font.render("Welcome to Sudoku", 1, title_color)
    title_rectangle = title_surface.get_rect(
        center=(600 // 2, 600 // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # to display game mode text
    gm_surface = gm_font.render("Select Game Mode:", 1, title_color)
    gm_rectangle = gm_surface.get_rect(
        center=(600 // 2, 600 // 2 - 40))
    screen.blit(gm_surface, gm_rectangle)

    # to display game mode buttons
    easy_text = button_font.render("EASY", 1, screen_color)
    med_text = button_font.render("MEDIUM", 1, screen_color)
    hard_text = button_font.render("HARD", 1, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20,
                                    easy_text.get_size()[1] + 20))
    easy_surface.fill(button_color)
    easy_surface.blit(easy_text, (10, 10))

    med_surface = pygame.Surface((med_text.get_size()[0] + 20,
                                 med_text.get_size()[1] + 20))
    med_surface.fill(button_color)
    med_surface.blit(med_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20,
                                  hard_text.get_size()[1] + 20))
    hard_surface.fill(button_color)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(600 // 2 - 200, 600 // 2 + 50))
    med_rectangle = med_surface.get_rect(
        center=(600 // 2, 600 // 2 + 50))
    hard_rectangle = hard_surface.get_rect(
        center=(600 // 2 + 200, 600 // 2 + 50))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # display level of difficulty of choice
    while True:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return 30
                elif med_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
def draw_game_won(screen):
    screen_color = (255, 255, 245)
    screen.fill(screen_color)
    title_color = (0, 33, 165)  # blue
    button_color = (250, 70, 22)  # orange

    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 60)

    # to display title mode
    title_surface = start_title_font.render("Game Won!", 1, title_color)
    title_rectangle = title_surface.get_rect(
        center=(600 // 2, 600 // 2 -40))
    screen.blit(title_surface, title_rectangle)

    button_text = button_font.render("Exit", 1, screen_color)
    button_surface = pygame.Surface((button_text.get_size()[0] + 20,
                                  button_text.get_size()[1] + 20))
    button_surface.fill(button_color)
    button_surface.blit(button_text, (10, 10))

    button_rectangle = button_surface.get_rect(
        center=(600 // 2, 600 // 2 + 50))
    screen.blit(button_surface, button_rectangle)
    while True:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rectangle.collidepoint(event.pos):
                    sys.exit()
def draw_game_over(screen):
    screen_color = (255, 255, 245)
    screen.fill(screen_color)
    title_color = (0, 33, 165)  # blue
    button_color = (250, 70, 22)  # orange

    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 60)

    # to display title mode
    title_surface = start_title_font.render("Game Over :(!", 1, title_color)
    title_rectangle = title_surface.get_rect(
        center=(600 // 2, 600 // 2 -40))
    screen.blit(title_surface, title_rectangle)

    button_text = button_font.render("Restart", 1, screen_color)
    button_surface = pygame.Surface((button_text.get_size()[0] + 20,
                                  button_text.get_size()[1] + 20))
    button_surface.fill(button_color)
    button_surface.blit(button_text, (10, 10))

    button_rectangle = button_surface.get_rect(
        center=(600 // 2, 600 // 2 + 50))
    screen.blit(button_surface, button_rectangle)
    while True:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rectangle.collidepoint(event.pos):
                    return draw_game_start(screen)
def main():
    game_over = False
    entered_num = None
    clicked_row = None
    clicked_col = None
    pygame.init()
    screen = pygame.display.set_mode((600, 640))
    pygame.display.set_caption("Sudoku")

    mode = draw_game_start(screen)
    sudoku_board = Board(600, 640, screen, mode)
    sudoku_board.draw()
    grid_num = generate_sudoku(9, mode)
    print("Grid num", grid_num)
    emp_coord = []
    i = 0
    j = 0
    buffer_row = 0
    for r_index, row in enumerate(grid_num):
        buffer = 0
        for c_index, col in enumerate(row):
            filling = Cell(col, r_index, c_index, screen)
            if filling.draw():
                emp_coord.append((c_index*66 + buffer, r_index*66 + buffer_row),)
            i += 1
            if i == 3:
                buffer += 6
                i = 0
        j += 1
        if j == 3:
            buffer_row += 6
            j = 0
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_row = int(event.pos[1]/64)
                clicked_col = int(event.pos[0]/64)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    entered_num = 1
                elif event.key == pygame.K_2:
                    entered_num = 2
                elif event.key == pygame.K_3:
                    entered_num = 3
                elif event.key == pygame.K_4:
                    entered_num = 4
                elif event.key == pygame.K_5:
                    entered_num = 5
                elif event.key == pygame.K_6:
                    entered_num = 6
                elif event.key == pygame.K_7:
                    entered_num = 7
                elif event.key == pygame.K_8:
                    entered_num = 8
                elif event.key == pygame.K_9:
                    entered_num = 9
                cell_fill = Cell(entered_num, clicked_row, clicked_col, screen)
                if cell_fill.set_sketched_value(grid_num):
                    if event.key == pygame.K_RETURN:
                        cell_fill.set_final_value(grid_num)
                        grid_num[clicked_row][clicked_col] = entered_num
                pygame.display.update()




if __name__ == "__main__":
    main()