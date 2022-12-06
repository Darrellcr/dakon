class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.cross = None
        self.value = value
        self.value.node = self

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None


    def add(self, valueTop, valueBottom) -> None:
        newNodeTop = Node(valueTop)
        newNodeBottom = Node(valueBottom)

        if self.head is None :
            self.head = newNodeTop
            self.tail = newNodeBottom
            self.head.next = self.tail
            self.tail.next = self.head
      
        # add top
        self.tail.next = newNodeTop
        self.tail = newNodeTop
        newNodeTop.next = self.head

        # add bottom
        tmp = self.head.next
        self.head.next = newNodeBottom
        newNodeBottom.next = tmp

    def edit(self, value) -> None:
        pass

    def delete(self) -> None:
        tmp = self.head

        while tmp.next is not self.tail :
            tmp = tmp.next
        
        # delete top
        self.tail = tmp
        tmp.next = self.head

        # delete bottom
        to_delete = self.head.next
        self.head.next = to_delete.next


