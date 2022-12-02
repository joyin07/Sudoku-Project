import pygame, sys
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
        center = (600 // 2, 600 // 2 + 50))
    hard_rectangle = hard_surface.get_rect(
        center=(600 // 2 + 200, 600 // 2 + 50))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return "easy"
                elif med_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    return "med"
                elif hard_rectangle.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()
def draw_in_game_screen(screen):
    screen_color = (209, 237, 242)
    screen.fill(screen_color)
    pygame.display.update()
def main():
    game_over = False
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")

    while True:
        for event in pygame.event.get():
            mode = draw_game_start(screen)
            pygame.display.update()
            print(mode)                     # have to delete
            if event.type == pygame.QUIT:
                sys.exit()
            if mode == "easy":
                removed_cells = 51
            elif mode == "med":
                removed_cells = 41
            elif mode == "hard":
                removed_cells = 31


if __name__ == "__main__":
    main()