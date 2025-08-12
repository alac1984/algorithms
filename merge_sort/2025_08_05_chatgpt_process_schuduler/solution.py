from node import Node
from linked_list import LinkedList


def merge_sort(llist: LinkedList) -> str:
    """
    A merge sort algorithm to sort LinkedList and returns
    a printed version of the sorting.
    """

    # Condition to stop division 
    if llist.size() == 1:
        return llist

    # Get the mid index
    mid = llist.size() // 2

    # Get the mid node
    mid_node = llist.traverse(mid)

    # Create the two lists
    right_half = LinkedList()
    right_head = mid_node.neighbor
    mid_node.del_neighbor()
    left_half = llist
    right_half.add_node(right_head)

    # Sort the lists
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Merge the lists
    return merge(left, right)


def merge(left: LinkedList, right: LinkedList) -> LinkedList:
    merged = LinkedList()
    tail = None
    a, b = left.head, right.head

    return a, b

    while a and b:
        if a.prio < b.prio:
            if a.pid < b.pid:
                merged.add_node(a)



if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.add(1, 10)
    llist1.add(2, 11)
    
    llist2 = LinkedList()
    llist2.add(3, 12)
    llist2.add(4, 13)
    llist2.add(5, 15)

    print(merge(llist1, llist2))
