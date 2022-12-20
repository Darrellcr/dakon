import pygame


class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.prev = None
        self.opposite = None
        self.value = value
        self.value.node = self


class CircularLinkedList:
    def __init__(self, square1, square2) -> None:
        square1.owner = 1
        square2.owner = 2
        self.head: Node = Node(square1)
        self.tail: Node = Node(square2)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head
        self.length = 2

    def add(self, pocket1, pocket2) -> None:
        self.length += 2
        pocket1.owner = 2
        pocket2.owner = 1
        newNodeTop = Node(pocket1)
        newNodeBottom = Node(pocket2)

        # add top
        prev_node: Node = self.head.prev
        next_node: Node = self.head
        newNodeTop.next = next_node
        newNodeTop.prev = prev_node
        next_node.prev = newNodeTop
        prev_node.next = newNodeTop

        # add bottom
        prev_node: Node = self.head
        next_node: Node = self.head.next
        newNodeBottom.next = next_node
        newNodeBottom.prev = prev_node
        next_node.prev = newNodeBottom
        prev_node.next = newNodeBottom

        newNodeTop.opposite = newNodeBottom
        newNodeBottom.opposite = newNodeTop

    def edit(self, pocket_num_marbles: int) -> None:
        # update jumlah marble pocket atas
        current: Node = self.head.prev
        while current is not self.tail:
            current.value.text = pocket_num_marbles
            current = current.prev

        # update jumlah marble pocket bawah
        current: Node = self.head.next
        while current is not self.tail:
            current.value.text = pocket_num_marbles
            current = current.next

    def delete(self) -> None:
        if self.length == 2:
            return
        self.length -= 2
        # delete top
        to_delete: Node = self.head.prev
        next_node: Node = self.head
        prev_node: Node = to_delete.prev
        next_node.prev = prev_node
        prev_node.next = next_node

        # delete bottom
        to_delete: Node = self.head.next
        next_node: Node = to_delete.next
        prev_node: Node = self.head
        next_node.prev = prev_node
        prev_node.next = next_node

    def draw(self, game):
        if self.length == 0:
            return
        self.head.value.draw(game)

        # draw top pockets
        current: Node = self.head.prev
        while current is not self.tail:
            current.value.draw(game)
            current = current.prev

        # draw bottom pockets
        current: Node = self.head.next
        while current is not self.tail:
            current.value.draw(game)
            current = current.next

        self.tail.value.draw(game)

    def is_end_game(self) -> bool:
        # checkTop
        is_all_empty = True
        current: Node = self.head.prev
        while current is not self.tail:
            if current.value.text > 0:
                is_all_empty = False
            current = current.prev

        if is_all_empty:
            return True

        # checkBottom
        is_all_empty = True
        current: Node = self.head.next
        while current is not self.tail:
            if current.value.text > 0:
                is_all_empty = False
            current = current.next

        return is_all_empty

    def get_winner(self) -> int:
        if self.head.value.text > self.tail.value.text:
            return self.head.value.owner
        return self.tail.value.owner

    def update_pocket_pos(self) -> None:
        num_pockets_per_row = (self.length - 2) // 2
        available = 530 // (num_pockets_per_row + 1)
        current_top: Node = self.tail.next
        current_bottom: Node = self.tail.prev
        for i in range(num_pockets_per_row):
            # update top
            current_top.value.box.container_rect.x = (
                135 + (available) * (i+1) - 25)
            current_top.value.box.text_rect = current_top.value.box.text_surf.get_rect(
                center=current_top.value.box.container_rect.center)
            current_top = current_top.next

            # update bottom
            current_bottom.value.box.container_rect.x = (
                135 + (available) * (i+1) - 25)
            current_bottom.value.box.text_rect = current_bottom.value.box.text_surf.get_rect(
                center=current_bottom.value.box.container_rect.center)
            current_bottom = current_bottom.prev

    def capture_opposite(self, node: Node):
        if node.value.owner == 1:
            self.head.value.text += node.opposite.value.text + 1
        else:
            self.tail.value.text += node.opposite.value.text + 1
        node.opposite.value.text = 0
        node.value.text = 0