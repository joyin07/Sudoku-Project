import pygame, sys
from Board import *
from sudoku_generator import *
from cell import *
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
                    main()
def draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid):
    sudoku_board = Board(600, 640, screen, mode)
    sudoku_board.draw()
    i = 0
    j = 0
    buffer_row = 0
    for r_index, row in enumerate(grid_num):
        buffer = 0
        for c_index, col in enumerate(row):
            if user_submit_grid[r_index][c_index] == 0:
                filling = Cell(col, r_index, c_index, screen)
                if filling.draw():
                    emp_coord.append((c_index * 66 + buffer, r_index * 66 + buffer_row), )
                i += 1
                if i == 3:
                    buffer += 6
                    i = 0
        j += 1
        if j == 3:
            buffer_row += 6
            j = 0
def compute_grid(sketched_value_grid, screen, grid_num, user_submit_grid, entered_num):
    for sketch_row_index, sketch_value_row in enumerate(sketched_value_grid):
        for sketch_col_index, sketch_value_col in enumerate(sketch_value_row):
            if sketch_value_col != 0:
                cell_fill = Cell(sketch_value_col, sketch_row_index, sketch_col_index, screen)
                cell_fill.set_sketched_value(grid_num)
    for final_row_index, final_value_row in enumerate(user_submit_grid):
        for final_col_index, final_value_col in enumerate(final_value_row):
            if final_value_col != 0:
                cell_fill = Cell(entered_num, final_row_index, final_col_index, screen)
                cell_fill.set_final_value(user_submit_grid)
    bottom_buttons(screen)
def bottom_buttons(screen):
    button_color = (250, 70, 22)  # orange
    button_font = pygame.font.Font(None, 30)

    button1_text = button_font.render("Reset", 1, (255, 255, 245))
    button_surface = pygame.Surface((button1_text.get_size()[0] + 10,
                                     button1_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button1_text, (5, 5))

    button1_rectangle = button_surface.get_rect(
        center=(100, 620))
    screen.blit(button_surface, button1_rectangle)

    button2_text = button_font.render("Restart", 1, (255, 255, 245))
    button_surface = pygame.Surface((button2_text.get_size()[0] + 10,
                                     button2_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button2_text, (5, 5))

    button2_rectangle = button_surface.get_rect(
        center=(300, 620))
    screen.blit(button_surface, button2_rectangle)

    button2_text = button_font.render("Restart", 1, (255, 255, 245))
    button_surface = pygame.Surface((button2_text.get_size()[0] + 10,
                                     button2_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button2_text, (5, 5))

    button3_text = button_font.render("Exit", 1, (255, 255, 245))
    button_surface = pygame.Surface((button3_text.get_size()[0] + 10,
                                     button3_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button3_text, (5, 5))
    button3_rectangle = button_surface.get_rect(
        center=(500, 620))
    screen.blit(button_surface, button3_rectangle)
def borders_command(clicked_row, clicked_col, screen):
    first_cell = Cell(None, clicked_row, clicked_col, screen)
    color = (217, 33, 33)
    first_cell.draw_border(clicked_row, clicked_col, color)
def checking_offscreen(row, col, screen):
    greatest = 8
    least = 0
    if col > greatest or row > greatest or col < least or row < least:
        return True
    return False
def checking_board_full(grid_num, user_submit_grid):
    for r_index, row in enumerate(grid_num):
        for c_index, col in enumerate(row):
            if col == 0:
                if user_submit_grid[r_index][c_index] == 0:
                    return False
    return True

def checking_win_or_lose(grid_num, user_submit_grid, screen):
    for r_index, row in enumerate(grid_num):
        for c_index, col in enumerate(row):
            if col == 0:
                grid_num[r_index][c_index] = user_submit_grid[r_index][c_index]
    print(grid_num)
    checking = Board(None, None, None, None)
    for index1, row1 in enumerate(grid_num):
        for index2, col1 in enumerate(row1):
            if not checking.check_board(index1, index2, grid_num):
                draw_game_over(screen)
                return False
    draw_game_won(screen)
    return True

def main():
    game_cont = True
    entered_num = 0
    clicked_row = None
    clicked_col = None
    pygame.init()
    screen = pygame.display.set_mode((600, 640))
    pygame.display.set_caption("Sudoku")
    sketched_value_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    user_submit_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    mode = draw_game_start(screen)
    # sudoku_board = Board(600, 640, screen, mode)
    # sudoku_board.draw()
    grid_num = generate_sudoku(9, mode)
    #solution = SudokuGenerator(9, mode)
    #solution.fill_values()
    #solution_board = solution.get_board()
    #print("solution board:", solution_board)
    print("Grid num", grid_num)
    emp_coord = []
    draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
    button_color = (250, 70, 22)  # orange
    button_font = pygame.font.Font(None, 30)

    button1_text = button_font.render("Reset", 1, (255, 255, 245))
    button_surface = pygame.Surface((button1_text.get_size()[0] + 10,
                                     button1_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button1_text, (5, 5))

    button1_rectangle = button_surface.get_rect(
        center=(100, 620))
    screen.blit(button_surface, button1_rectangle)

    button2_text = button_font.render("Restart", 1, (255, 255, 245))
    button_surface = pygame.Surface((button2_text.get_size()[0] + 10,
                                     button2_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button2_text, (5, 5))

    button2_rectangle = button_surface.get_rect(
        center=(300, 620))
    screen.blit(button_surface, button2_rectangle)

    button2_text = button_font.render("Restart", 1, (255, 255, 245))
    button_surface = pygame.Surface((button2_text.get_size()[0] + 10,
                                     button2_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button2_text, (5, 5))

    button3_text = button_font.render("Exit", 1, (255, 255, 245))
    button_surface = pygame.Surface((button3_text.get_size()[0] + 10,
                                     button3_text.get_size()[1] + 10))
    button_surface.fill(button_color)
    button_surface.blit(button3_text, (5, 5))
    button3_rectangle = button_surface.get_rect(
        center=(500, 620))
    screen.blit(button_surface, button3_rectangle)

    while game_cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_row = int(event.pos[1]//67)
                clicked_col = int(event.pos[0]//67)

                draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
                compute_grid(sketched_value_grid, screen, grid_num, user_submit_grid, entered_num)
                if button1_rectangle.collidepoint(event.pos):
                    draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
                    bottom_buttons(screen)
                    sketched_value_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

                    user_submit_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                elif button2_rectangle.collidepoint(event.pos):
                    main()
                elif button3_rectangle.collidepoint(event.pos):
                    sys.exit()
                else:
                    borders_command(clicked_row, clicked_col, screen)

            if event.type == pygame.KEYDOWN:
                num_entered = False
                if event.key == pygame.K_1:
                    entered_num = 1
                    num_entered = True
                elif event.key == pygame.K_2:
                    entered_num = 2
                    num_entered = True
                elif event.key == pygame.K_3:
                    entered_num = 3
                    num_entered = True
                elif event.key == pygame.K_4:
                    entered_num = 4
                    num_entered = True
                elif event.key == pygame.K_5:
                    entered_num = 5
                    num_entered = True
                elif event.key == pygame.K_6:
                    entered_num = 6
                    num_entered = True
                elif event.key == pygame.K_7:
                    entered_num = 7
                    num_entered = True
                elif event.key == pygame.K_8:
                    entered_num = 8
                    num_entered = True
                elif event.key == pygame.K_9:
                    entered_num = 9
                    num_entered = True
                elif event.key == pygame.K_RETURN:
                    cell_fill = Cell(None, clicked_row, clicked_col, screen)
                    cell_fill.set_final_value(sketched_value_grid)
                    user_submit_grid[clicked_row][clicked_col] = sketched_value_grid[clicked_row][clicked_col]
                    pygame.display.update()
                    if checking_board_full(grid_num, user_submit_grid):
                        if checking_win_or_lose(grid_num, user_submit_grid, screen):
                            game_cont = False
                elif event.key == pygame.K_RIGHT:
                    clicked_col += 1
                    if checking_offscreen(clicked_row, clicked_col, screen):
                        clicked_col -= 1
                    draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
                    compute_grid(sketched_value_grid, screen, grid_num, user_submit_grid, entered_num)
                    borders_command(clicked_row, clicked_col, screen)
                elif event.key == pygame.K_LEFT:
                    clicked_col -= 1
                    if checking_offscreen(clicked_row, clicked_col, screen):
                        clicked_col += 1
                    draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
                    compute_grid(sketched_value_grid, screen, grid_num, user_submit_grid, entered_num)
                    borders_command(clicked_row, clicked_col, screen)
                elif event.key == pygame.K_UP:
                    clicked_row -= 1
                    if checking_offscreen(clicked_row, clicked_col, screen):
                        clicked_row += 1
                    draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
                    compute_grid(sketched_value_grid, screen, grid_num, user_submit_grid, entered_num)
                    borders_command(clicked_row, clicked_col, screen)
                elif event.key == pygame.K_DOWN:
                    clicked_row += 1
                    if checking_offscreen(clicked_row, clicked_col, screen):
                        clicked_row -= 1
                    draw_game_screen(screen, grid_num, emp_coord, mode, user_submit_grid)
                    compute_grid(sketched_value_grid, screen, grid_num, user_submit_grid, entered_num)
                    borders_command(clicked_row, clicked_col, screen)
                else:
                    print("Invalid Number")
                    continue

                if num_entered:
                    cell_fill = Cell(entered_num, clicked_row, clicked_col, screen)
                    if cell_fill.set_sketched_value(grid_num):
                        sketched_value_grid[clicked_row][clicked_col] = entered_num
                        if event.key == pygame.K_RETURN:
                            cell_fill.set_final_value(sketched_value_grid)
                            user_submit_grid[clicked_row][clicked_col] = sketched_value_grid[clicked_row][clicked_col]
                            if checking_board_full(grid_num, user_submit_grid):
                                if checking_win_or_lose(grid_num, user_submit_grid, screen):
                                    game_cont = False
            pygame.display.update()




if __name__ == "__main__":
    main()