import pygame
from abc import abstractclassmethod, ABC
import time


class Square:
    def __init__(
        self,
        text,
        size: tuple[int, int],
        pos: tuple[int, int],
        color,
        font_color='#FFFFFF',
        font_size=25
    ) -> None:
        # container
        self.container_rect = pygame.Rect(pos, size)
        self.container_color = color
        # content
        self._text = text
        self.font = pygame.font.SysFont('candara', font_size)
        self.font.set_bold(True)
        self.font_color = font_color
        self.text_surf = self.font.render(
            f'{self._text}', True, self.font_color)
        self.text_rect = self.text_surf.get_rect(
            center=self.container_rect.center)
        self.node = None
        self.owner = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, val):
        self._text = val
        self.update_text()

    def draw(self, game) -> None:
        pygame.draw.rect(game.screen, self.container_color,
                         self.container_rect, border_radius=8)
        game.screen.blit(self.text_surf, self.text_rect)

    def update_text(self) -> None:
        self.text_surf = self.font.render(
            f'{self.text}', True, self.font_color)
        self.text_rect = self.text_surf.get_rect(
            center=self.container_rect.center)

    def increase(self) -> None:
        self._text += 1
        self.update_text()

    def decrease(self) -> None:
        self._text -= 1
        self.update_text()


class Pocket:
    def __init__(
        self,
        text,
        size: tuple[int, int],
        pos: tuple[int, int],
        color,
        on_hover_color,
        on_click_color,
        font_color='#FFFFFF'
    ) -> None:
        self.box = Square(text, size, pos, color, font_color)
        self.is_clicked = False
        self.default_color = color
        self.on_hover_color = on_hover_color
        self.on_click_color = on_click_color

        self.marble_drop_sound = pygame.mixer.Sound('./assets/marble_drop.wav')
        pygame.mixer.Sound.set_volume(self.marble_drop_sound, 0.5)
        self.capture_sound = pygame.mixer.Sound('./assets/capture_sound.wav')
        pygame.mixer.Sound.set_volume(self.capture_sound, 0.8)

        self.click_disabled = False

    @property
    def node(self):
        return self.box.node

    @node.setter
    def node(self, n):
        self.box.node = n

    @property
    def owner(self):
        return self.box.owner

    @owner.setter
    def owner(self, owner):
        self.box.owner = owner

    @property
    def text(self):
        return self.box.text

    @text.setter
    def text(self, value):
        self.box.text = value
        self.box.update_text()

    def draw(self, game) -> None:
        self.check_clicked(game)
        self.box.draw(game)

    def is_hovered(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if self.box.container_rect.collidepoint(mouse_pos):
            self.box.container_color = self.on_hover_color
            return True
        self.box.container_color = self.default_color
        return False

    def check_clicked(self, game) -> None:
        if (game.is_player1_turn and self.owner == 2) \
            or (not game.is_player1_turn and self.owner == 1) \
            or self.click_disabled or self.box.text == 0:
            return
        is_hovered = self.is_hovered()
        if is_hovered and pygame.mouse.get_pressed()[0]:
            self.box.container_color = self.on_click_color
            if not self.is_clicked:
                self.click(game)
                self.is_clicked = True
        elif not is_hovered:
            self.box.container_color = self.default_color

        if not pygame.mouse.get_pressed()[0]:
            self.is_clicked = False

    def click(self, game) -> None:
        """
        hal yang terjadi kalo diklik
        """
        num_marbles = self.box.text
        self.box.text = 0
        self.click_disabled = True
        self.box.container_color = self.default_color
        self.draw(game)
        self.click_disabled = False
        pygame.display.update()
        current_node = self.node.prev
        for _ in range(num_marbles):
            current_node.value.increase()
            self.play_marble_drop_sound()
            current_node.value.click_disabled = True
            current_node.value.draw(game)
            current_node.value.click_disabled = False
            pygame.display.update()
            time.sleep(0.4)
            current_node = current_node.prev
        last_node_added = current_node.next
        if isinstance(last_node_added.value, Square):
            return
        opposite_node = last_node_added.opposite
        if opposite_node.value.text > 0 and last_node_added.value.text == 1 and (
            (last_node_added.value.owner == 1 and game.is_player1_turn) or 
            (last_node_added.value.owner == 2 and not game.is_player1_turn)):
            game.linkedlist.capture_opposite(last_node_added)
            self.play_capture_sound()
        self.update_turn(game)
            
    def update_turn(self, game) -> None:
        game.is_player1_turn = not game.is_player1_turn
        if game.is_player1_turn:
            game.square_player_turn.text = 'Turn player 1 (bottom)'
        else:
            game.square_player_turn.text = 'Turn player 2 (top)'


    def play_marble_drop_sound(self) -> None:
        pygame.mixer.Sound.play(self.marble_drop_sound)
    
    def play_capture_sound(self) -> None:
        pygame.mixer.Sound.play(self.capture_sound)

    def increase(self) -> None:
        self.box.increase()

    def decrease(self) -> None:
        self.box.decrease()

    def update_x_position(self, x) -> None:
        self.box.container_rect.x = x


class Arrow(ABC):
    def __init__(
        self,
        size: tuple[int, int],
        pos: tuple[int, int],
        color,
        on_hover_color,
        on_click_color,
        box_to_update: Square
    ) -> None:
        # container
        self.container_rect = pygame.Rect(pos, size)

        # triangle color
        self.current_color = color
        self.default_color = color
        self.on_hover_color = on_hover_color
        self.on_click_color = on_click_color

        self.box_to_update = box_to_update

        self.is_clicked = False

    def draw(self, surface) -> None:
        self.check_clicked()

    def is_hovered(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if self.container_rect.collidepoint(mouse_pos):
            self.current_color = self.on_hover_color
            return True
        self.current_color = self.default_color
        return False

    def check_clicked(self) -> None:
        is_hovered = self.is_hovered()
        if is_hovered and pygame.mouse.get_pressed()[0]:
            self.current_color = self.on_click_color
            if not self.is_clicked:
                self.click()
                self.is_clicked = True
        elif not is_hovered:
            self.current_color = self.default_color

        if not pygame.mouse.get_pressed()[0]:
            self.is_clicked = False

    @abstractclassmethod
    def click(self) -> None:
        pass


class ArrowUp(Arrow):
    def __init__(
        self,
        size: tuple[int, int],
        pos: tuple[int, int],
        color,
        on_hover_color,
        on_click_color,
        box_to_update: Square
    ) -> None:
        super().__init__(size, pos, color, on_hover_color, on_click_color, box_to_update)

    def draw(self, surface) -> None:
        super().draw(surface)
        pygame.draw.polygon(surface, self.current_color, (
            (self.container_rect.center[0], self.container_rect.top),
            self.container_rect.bottomleft,
            self.container_rect.bottomright))

    def click(self) -> None:
        if self.box_to_update.text > 7:
            return
        self.box_to_update.increase()


class ArrowDown(Arrow):
    def __init__(
        self,
        size: tuple[int, int],
        pos: tuple[int, int],
        color,
        on_hover_color,
        on_click_color,
        box_to_update: Square
    ) -> None:
        super().__init__(size, pos, color, on_hover_color, on_click_color, box_to_update)

    def draw(self, surface) -> None:
        super().draw(surface)
        pygame.draw.polygon(surface, self.current_color, (
            self.container_rect.topright,
            self.container_rect.topleft,
            (self.container_rect.center[0], self.container_rect.bottom)
        ))

    def click(self) -> None:
        if self.box_to_update.text < 5:
            return
        self.box_to_update.decrease()

# if __name__ == "__main__":
#     for i in pygame.colordict.THECOLORS.keys():
#         print(i)
