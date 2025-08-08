"""Implementing LinkedList"""

from node import Node

class LinkedList:

    # TODO: create a method connect_head that connects a head in the
    # LinkedList with validations.

    def __init__(self) -> None:
        """
        Instantiate an empty LinkedList.
        """

        self.head = None

    def _add_head(self, node: Node) -> None:
        """
        Internal method to validate head addition.
        """

        if node.neighbor != self.head:
            raise ValueError("A Node with neighbor could not be a LinkedList head.")

        self.head = node

    def is_empty(self) -> bool:
        """
        Checks if a LinkedList is empty (if there's no head, it
        is empty).
        """

        return self.head is None

    def add(self, pid: int, prio: int) -> None:
        """
        Adds a new Node on the head and pushes the former head
        to the right.
        """

        new_node = Node(pid, prio)

        if self.head is not None:
            new_node.set_neighbor(self.head)

        self._add_head(new_node)

    def add_node(self, node: Node) -> None:
        """
        Adds a preexisting Node on the head after validate if the node has
        no neighbor.
        """

        if self.head:
            node.set_neighbor(self.head)

        self._add_head(node)

    def size(self) -> int:
        """
        Returns the size of the list.

        Runs in O(n) time and O(1) space.
        """

        current = self.head

        count = 0
        while current:
            count += 1
            current = current.neighbor

        return count

    def sort(self) -> None:
        ...

        # TODO: Method

    def traverse(self, index: int) -> Node:
        """
        Returns the node at a given index.

        Runs in O(n) time and O(1) space.
        """

        if index < 0 or index > self.size():
            raise ValueError("Index out of bound")
        
        current = self.head
        count = 0

        while count < index:
            count += 1
            current = current.neighbor
        else:
            return current

    def __repr__(self) -> str:
        """
        String representation of a LinkedList.
        """

        current = self.head
        if not current:
            return f"<Head: None>"

        result = f"<Head: pid {current.pid} | prio {current.prio}>"

        if current.has_neighbor():
            result += " → "

        current = current.neighbor

        while current:
            if not current.has_neighbor():
                result += f"<Tail: pid {current.pid} | prio {current.prio}>"
                break
            else:
                result += f"<pid {current.pid} | prio {current.prio}> → "
                current = current.neighbor

        return result
