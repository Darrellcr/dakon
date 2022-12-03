import game

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 500


def main() -> None:
    dakon = game.Game((SCREEN_WIDTH, SCREEN_HEIGHT))
    while dakon.is_running:
        dakon.game_loop()
        dakon.menu.display()


if __name__ == "__main__":
    main()
