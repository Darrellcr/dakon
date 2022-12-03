import pygame
from abc import abstractclassmethod, ABC


class Square:
    def __init__(
        self,
        text,
        size: tuple[int, int],
        pos: tuple[int, int],
        color
    ) -> None:
        # container
        self.container_rect = pygame.Rect(pos, size)
        self.container_color = color
        # content
        self.text = text
        self.font = pygame.font.SysFont('candara', 25)
        self.font.set_bold(True)
        self.text_surf = self.font.render(f'{self.text}', True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(
            center=self.container_rect.center)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.container_color,
                         self.container_rect, border_radius=8)
        surface.blit(self.text_surf, self.text_rect)

    def update_text(self) -> None:
        self.text_surf = self.font.render(f'{self.text}', True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(
            center=self.container_rect.center)

    def increase(self) -> None:
        self.text += 1
        self.update_text()

    def decrease(self) -> None:
        self.text -= 1
        self.update_text()


class Pocket:
    def __init__(
        self,
        text,
        size: tuple[int, int],
        pos: tuple[int, int],
        color,
        on_hover_color,
        on_click_color
    ) -> None:
        self.box = Square(text, size, pos, color)
        self.is_clicked = False
        self.default_color = color
        self.on_hover_color = on_hover_color
        self.on_click_color = on_click_color

    def draw(self, surface: pygame.Surface) -> None:
        self.check_clicked()
        self.box.draw(surface)

    def is_hovered(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if self.box.container_rect.collidepoint(mouse_pos):
            self.box.container_color = self.on_hover_color
            return True
        self.box.container_color = self.default_color
        return False

    def check_clicked(self) -> None:
        is_hovered = self.is_hovered()
        if is_hovered and pygame.mouse.get_pressed()[0]:
            self.box.container_color = self.on_click_color
            if not self.is_clicked:
                self.click()
                self.is_clicked = True
        elif not is_hovered:
            self.box.container_color = self.default_color

        if not pygame.mouse.get_pressed()[0]:
            self.is_clicked = False

    def click(self) -> None:
        """
        hal yang terjadi kalo diklik
        """
        self.box.increase()


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
    
    def check_clicked(self) -> None:
        self.box_to_update.decrease()

if __name__ == "__main__":
    for i in pygame.colordict.THECOLORS.keys():
        print(i)
