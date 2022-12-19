import pygame

from object import ArrowDown, ArrowUp, Pocket, Square

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill('#DCDDD8')
    pygame.display.set_caption('Button demo')

    buttonBottom =[]
    buttonTop = []
    jumlahButton = 8
    available = 530 // (jumlahButton + 1)

    for i in range (jumlahButton):
        buttonBottom.append(Pocket(
        text=0, 
        size=(50, 40), 
        pos=(135 + (available) * (i+1) - 25 , SCREEN_HEIGHT/2 + 150 - 40),
        color='blue',
        on_hover_color='green',
        on_click_color='red',))

        buttonTop.append(Pocket(  
        text=0, 
        size=(50, 40), 
        pos=(135 + (available) * (i+1) - 25, SCREEN_HEIGHT/2 - 150),
        color='blue',
        on_hover_color='green',
        on_click_color='red'))


    # button1 = Pocket(
    #     text=0, 
    #     size=(50, 40), 
    #     pos=(135 + 133  - 25, SCREEN_HEIGHT/2 - 150/2 - 80),
    #     color='blue',
    #     on_hover_color='green',
    #     on_click_color='red'
    #     )

    # button2 = Pocket(
    #     text=0, 
    #     size=(50, 40), 
    #     pos = (135 + 133 - 25 + 133 - 25, SCREEN_HEIGHT/2 + 150/2 + 50),
    #     color='blue',
    #     on_hover_color='green',
    #     on_click_color='red')

    # button3 = Pocket(
    #     text=0, 
    #     size=(50, 40), 
    #     pos = (135 + 133 - 25 + 133 - 25 + 133 - 25, SCREEN_HEIGHT/2 + 150/2 + 50),
    #     color='blue',
    #     on_hover_color='green',
    #     on_click_color='red')

    square1 = Square(
        text=10,
        size=(105, 150),
        pos=(30, SCREEN_HEIGHT/2 - 150/2),
        color=(255,255,0)
    )

    square2 = Square(
        text=0,
        size=(105, 150),
        pos=(SCREEN_WIDTH - 105 - 30, SCREEN_HEIGHT/2 - 150/2),
        color=(255,255,0)
    )

    arrow_up = ArrowUp(
        size=(30, 20),
        pos=(SCREEN_WIDTH-50, 10),
        color='red',
        on_hover_color='cyan',
        on_click_color='blue',
        box_to_update=square1
    )

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # button1.draw(screen)
        # button1.draw(screen)
        # button2.draw(screen)
        # button3.draw(screen)
        for j in buttonTop :
            j.draw(screen, True)
        for i in buttonBottom :
            i.draw(screen, True)
        arrow_up.draw(screen)
        square1.draw(screen, True)
        square2.draw(screen, True)
        # button1.draw(screen)
        # arrow_up.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
