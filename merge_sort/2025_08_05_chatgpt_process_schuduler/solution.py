from node import Node
from linked_list import LinkedList


def merge_sort(llist: LinkedList) -> str:
    """
    A merge sort algorithm to sort LinkedList and returns
    a printed version of the sorting.
    """

    # Casos base rápidos (evita custo de llist.size())
    if llist.head is None or llist.head.neighbor is None:
        return llist

    def split(head: Node) -> tuple[Node, Node]:
        """Divide a lista em duas metades [head..mid-1], [mid..] e corta o elo."""
        slow, fast = head, head.neighbor
        while fast and fast.neighbor:
            slow = slow.neighbor
            fast = fast.neighbor.neighbor
        mid = slow.neighbor
        slow.neighbor = None
        return head, mid

    def comes_before(a: Node, b: Node) -> bool:
        """Regra de ordenação estável: prio ASC, depois pid ASC; empates mantêm ordem."""
        if a.prio != b.prio:
            return a.prio < b.prio
        if a.pid != b.pid:
            return a.pid < b.pid
        return True  # estável: se tudo empata, mantém 'a' antes de 'b'

    def merge(a: Node, b: Node) -> Node:
        """Intercala duas listas já ordenadas, religando ponteiros (sem criar nós reais)."""
        dummy = Node(1, 0)  # sentinela (constante); prio/pid válidos
        tail = dummy
        while a and b:
            if comes_before(a, b):
                tail.neighbor, a = a, a.neighbor
            else:
                tail.neighbor, b = b, b.neighbor
            tail = tail.neighbor
        tail.neighbor = a if a else b
        head = dummy.neighbor
        dummy.neighbor = None  # opcional: solta referencia
        return head

    def sort(head: Node) -> Node:
        if head is None or head.neighbor is None:
            return head
        left, right = split(head)
        left = sort(left)
        right = sort(right)
        return merge(left, right)

    llist.head = sort(llist.head)
    return llist



if __name__ == "__main__":
    llist = LinkedList()
    llist.add(1, 10)
    llist.add(2, 11)
    llist.add(3, 12)
    llist.add(4, 13)
    llist.add(5, 15)

    print(merge_sort(llist))
