# Implementing Node class

class Node:

    def __init__(self, pid: int, prio: int):
        # Validations
        if pid < 1:
            raise ValueError("pid value is less than 1")

        if pid > 10**9:
            raise ValueError("pid value is over 10**9")

        if prio < 0:
            raise ValueError("prio value is less than 0")

        if prio > 10**5:
            raise ValueError("prio value is over 10**5")

        # Initialization
        self.pid = pid
        self.prio = prio
        self.neighbor = None

    def set_neighbor(self, neighbor: 'Node'):
        """A method to set a neighbor with necessary validation"""

        if not isinstance(neighbor, Node):
            raise TypeError("neighbor should be of type Node")

        self.neighbor = neighbor

    def has_neighbor(self) -> bool:
        """A method that retrieves if the Node has a neighbor"""

        return self.neighbor is not None

    def __eq__(self, other: 'Node'):
        """Determine if a Node is equal to other"""
        if not isinstance(other, Node):
            raise TypeError("Node type can be only compared to itself.")

        return self.pid == other.pid and self.prio == other.prio

    def __repr__(self):
        """String representation of a Node"""

        return f"<Node: pid {self.pid} | prio {self.prio}>"
