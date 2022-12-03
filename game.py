import pygame


class Game:
    def __init__(self, screen_size: tuple[int, int]) -> None:
        pygame.init()
        self.is_running = True
        self.is_playing = True

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Dakon')
        self.menu = Menu(self)

        self.pocket_counts = 6

    def game_loop(self) -> None:
        self.screen.fill('#DCDDD8')  # bg color
        while self.is_playing:
            self.check_events()
            pygame.display.update()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_playing = False
                    self.menu.is_displaying = True

    def reset_game(self) -> None:
        pass


class Menu:
    def __init__(self, g: Game) -> None:
        self.game: Game = g
        self.is_displaying = False

    def display(self) -> None:
        self.game.screen.fill('#000000')  # bg color
        while self.is_displaying:
            self.check_events()
            pygame.display.update()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_displaying = False
                self.game.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.reset_game()
                    self.game.is_playing = True
                    self.is_displaying = False
