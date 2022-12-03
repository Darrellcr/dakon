import pygame

from object import ArrowDown, ArrowUp, Pocket, Square

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill('#DCDDD8')
    pygame.display.set_caption('Button demo')
    button = Pocket(
        text=0, 
        size=(50, 40), 
        pos=(SCREEN_WIDTH/2-70, SCREEN_HEIGHT/2-30),
        color='blue',
        on_hover_color='green',
        on_click_color='red')
    button1 = Pocket(
        text=0, 
        size=(50, 40),
        pos=(SCREEN_WIDTH/2+20, SCREEN_HEIGHT/2-30),
        color='blue',
        on_hover_color='green',
        on_click_color='red')

    square = Square(
        text=10,
        size=(70, 100),
        pos=(10, 10),
        color=(255,255,0)
    )

    arrow_up = ArrowUp(
        size=(30, 20),
        pos=(SCREEN_WIDTH-50, 10),
        color='red',
        on_hover_color='cyan',
        on_click_color='blue',
        box_to_update=square
    )

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        button1.draw(screen)
        button.draw(screen)
        square.draw(screen)
        arrow_up.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
