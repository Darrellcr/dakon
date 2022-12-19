import game

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 500


def main() -> None:
    dakon = game.Game((SCREEN_WIDTH, SCREEN_HEIGHT))
    while dakon.is_running:
        dakon.game_loop()
        if dakon.is_end_game():
            winner = dakon.get_winner()
            print(f"Player {winner} win!")
            return
        dakon.menu.display()


if __name__ == "__main__":
    main()
