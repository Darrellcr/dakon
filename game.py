import pygame
from object import ArrowUp, ArrowDown, Square, Pocket
from linkedlist import CircularLinkedList


class Game:
    def __init__(self, screen_size: tuple[int, int]) -> None:
        pygame.init()
        self.is_running = True
        self.is_playing = True

        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Dakon')
        self.menu = Menu(self)

        self.create_linkedlist()
        self.is_player1_turn = True

    def game_loop(self) -> None:
        self.screen.fill('#DCDDD8')  # bg color
        while self.is_playing:
            self.check_events()
            self.linkedlist.draw(self)
            self.square_player_turn.draw(self)
            pygame.display.update()
            if self.is_end_game():
                break

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_playing = False
                    self.menu.is_displaying = True

    def create_linkedlist(self) -> None:   
        self.square_player_turn = Square("Turn player 1 (bottom)", (260, 50), (self.screen_width/2-130, self.screen_height/2-25), '#DCDDD8', 'black', 22)  
        square1 = Square(
            text=0,
            size=(105, 150),
            pos=(self.screen_width - 105 - 30, self.screen_height/2 - 150/2),
            color='#4d2e07'
        )
        square2 = Square(
            text=0,
            size=(105, 150),
            pos=(30, self.screen_height/2 - 150/2),
            color='#4d2e07'
        )
        self.linkedlist = CircularLinkedList(square1, square2)
        jumlah_pocket = 5
        available = 530 // (jumlah_pocket + 1)
        for i in range(jumlah_pocket):
            self.linkedlist.add(
                pocket1=Pocket(
                    text=5,
                    size=(50, 40),
                    pos=(135 + (available) * (i+1) - 25,
                         self.screen_height/2 - 150),
                    color='#903b0d',
                    on_hover_color='#a97b4c',
                    on_click_color='blue'),
                pocket2=Pocket(
                    text=5,
                    size=(50, 40),
                    pos=(135 + (available) * (i+1) - 25,
                         self.screen_height/2 + 150 - 40),
                    color='#903b0d',
                    on_hover_color='#a97b4c',
                    on_click_color='blue')
            )
    
    def is_end_game(self) -> bool:
        return self.linkedlist.is_end_game()

    def get_winner(self) -> int:
        return self.linkedlist.get_winner()


class Menu:
    def __init__(self, g: Game) -> None:
        self.game: Game = g
        self.is_displaying = False

        # create object menu
        self.squareBiji = Square(
            text="Biji dakon",
            size=(190, 100),
            pos=(70, 90),
            color="#AFBFDB",
        )

        self.squareArena = Square(
            text="Arena dakon",
            size=(190, 100),
            pos=(70, 300),
            color="#AFBFDB"
        )

        self.squarePanahAtas = Square(
            text="->",
            size=(40, 40),
            pos=(290, 120),
            color="black",
        )

        self.squarePanahBawah = Square(
            text="->",
            size=(40, 40),
            pos=(290, 330),
            color="black",
        )

        self.squareJumlah1 = Square(
            text=5,
            size=(190, 100),
            pos=(360, 90),
            color="#B5E3D2",
        )

        self.squareJumlah2 = Square(
            text=5,
            size=(190, 100),
            pos=(360, 300),
            color="#B5E3D2",
        )

        self.arrowBijiUp = ArrowUp(
            size=(80, 40),
            pos=(570, 90),
            color="#C46AC0",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah1
        )

        self.arrowBijidown = ArrowDown(
            size=(80, 40),
            pos=(570, 150),
            color="#C46AC0",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah1
        )

        self.arrowArenaUp = ArrowUp(
            size=(80, 40),
            pos=(570, 300),
            color="#C46AC0",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah2
        )

        self.arrowArenaDown = ArrowDown(
            size=(80, 40),
            pos=(570, 360),
            color="#C46AC0",
            on_hover_color="#030202",
            on_click_color="#D195ED",
            box_to_update=self.squareJumlah2
        )

    def display(self) -> None:
        self.game.screen.fill('#FF9E9E')  # bg color
        while self.is_displaying:
            self.check_events()

            # draw object menu
            self.squareBiji.draw(self.game)
            self.squareArena.draw(self.game)
            self.squarePanahAtas.draw(self.game)
            self.squarePanahBawah.draw(self.game)
            self.squareJumlah1.draw(self.game)
            self.squareJumlah2.draw(self.game)
            self.arrowBijiUp.draw(self.game.screen)
            self.arrowBijidown.draw(self.game.screen)
            self.arrowArenaUp.draw(self.game.screen)
            self.arrowArenaDown.draw(self.game.screen)

            pygame.display.update()
        self.update_game_object()
        self.game.is_player1_turn = True

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_displaying = False
                self.game.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.is_playing = True
                    self.is_displaying = False

    def update_game_object(self) -> None:
        # ketika pocket ditambah
        while self.game.linkedlist.length-2 < self.squareJumlah2.text * 2:
            self.game.linkedlist.add(
                pocket1=Pocket(
                    text=5,
                    size=(50, 40),
                    pos=(0,
                         self.game.screen_height/2 - 150),
                    color='#903b0d',
                    on_hover_color='#a97b4c',
                    on_click_color='blue'),
                pocket2=Pocket(
                    text=5,
                    size=(50, 40),
                    pos=(0,
                         self.game.screen_height/2 + 150 - 40),
                    color='#903b0d',
                    on_hover_color='#a97b4c',
                    on_click_color='blue')
            )
        # ketika pocket dikurangi
        while self.game.linkedlist.length-2 > self.squareJumlah2.text * 2:
            self.game.linkedlist.delete()
        self.game.linkedlist.update_pocket_pos()
        self.game.linkedlist.edit(self.squareJumlah1.text)

        self.game.linkedlist.head.value.text = 0
        self.game.linkedlist.tail.value.text = 0
