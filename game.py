import pygame
from object import ArrowUp, ArrowDown, Square


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

        # create object menu
        self.squareBiji = Square(
        text = "Biji dakon",
        size = (190,100),
        pos = (70,90),
        color = "#C0EEE4",
        font_color="black"
        )

        self.squareArena = Square(
            text = "Arena dakon",
            size=(190,100),
            pos=(70,300),
            color="#C0EEE4",
            font_color="black"
        )

        self.squarePanahAtas = Square(
        text =  "->",
        size = (40,40),
        pos = (290,120),
        color = "#B6E2A1",
        )

        self.squarePanahBawah = Square(
        text =  "->",
        size = (40,40),
        pos = (290,330),
        color = "#B6E2A1",
        )

        self.squareJumlah1 = Square(
        text = 5,
        size = (190,100),
        pos = (360,90),
        color = "#C0EEE4",
        font_color="black"
        )

        self.squareJumlah2 = Square(
        text = 5,
        size = (190,100),
        pos = (360,300),
        color = "#C0EEE4",
        font_color="black"

        )

        self.arrowBijiUp = ArrowUp(
            size=(80,40),
            pos=(570,90),
            color="#F8F988",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah1
        )

        self.arrowBijidown = ArrowDown(
            size=(80,40),
            pos=(570,150),
            color="#F8F988",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah1
        )

        self.arrowArenaUp = ArrowUp(
            size=(80,40),
            pos=(570,300),
            color="#F8F988",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah2
        )

        self.arrowArenaDown = ArrowDown(
            size=(80,40),
            pos=(570,360),
            color="#F8F988",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah2
        )


    def display(self) -> None:
        self.game.screen.fill('#FF9E9E')  # bg color
        while self.is_displaying:
            self.check_events()

            # draw object menu
            self.squareBiji.draw(self.game.screen)
            self.squareArena.draw(self.game.screen)
            self.squarePanahAtas.draw(self.game.screen)
            self.squarePanahBawah.draw(self.game.screen)
            self.squareJumlah1.draw(self.game.screen)
            self.squareJumlah2.draw(self.game.screen)
            self.arrowBijiUp.draw(self.game.screen)
            self.arrowBijidown.draw(self.game.screen)
            self.arrowArenaUp.draw(self.game.screen)
            self.arrowArenaDown.draw(self.game.screen)

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
