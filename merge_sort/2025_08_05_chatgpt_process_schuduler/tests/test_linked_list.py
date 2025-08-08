# LinkedList tests

import pytest
from node import Node
from linked_list import LinkedList

def test_linkedlist_init_success():
    """
    Test a LinkedList being successfuly instantiated.
    """

    llist = LinkedList()

    assert llist is not None
    assert llist.head is None


def test_linkedlist_is_empty_success():
    """
    Test LinkedList method is_empty returning True if a LinkedList
    is empty.
    """

    llist = LinkedList()
    assert llist.is_empty() is True

def test_linkedlist_is_empty_failure():
    """
    Test LinkedList method is_empty returning False if a LinkedList
    is not empty.
    """

    llist = LinkedList()
    llist.add(1, 10)

    assert llist.is_empty() is False

def test_linkedlist_add_success():
    """
    Test LinkedList method add adding with success correct values.
    """

    llist = LinkedList()
    llist.add(1, 10)

    assert llist.head is not None
    assert llist.head == Node(1, 10)

def test_linkedlist_add_failure_pid_over_max():
    """
    Test LinkedList method add propagates Node's errors.
    """

    with pytest.raises(ValueError, match=r"pid value is over 10\*\*9"):
        llist = LinkedList()
        llist.add(10**10, 10)

def test_linkedlist_add_node_success():
    """
    Test LinkedList method add_node with a possible Node.
    """
    node = Node(10, 10)
    assert node.has_neighbor() is False

    llist = LinkedList()
    llist.add_node(node)

    assert llist.head == node


def test_linkedlist_add_node_failure():
    """
    Test LinkedList method add_node with a Node not eligible for
    addition (i.e. the Node already has a neighbor.)
    """

    n1 = Node(10, 10)
    n2 = Node(11, 11)
    n1.set_neighbor(n2)

    assert n1.has_neighbor() is True

    llist = LinkedList()
    with pytest.raises(ValueError, match="A Node with neighbor could not be a LinkedList head."):
        llist.add_node(n1)


def test_linkedlist_size_zero_node():
    """
    Test LinkedList method size with a empty LinkedList.
    """

    llist = LinkedList()
    assert llist.size() == 0


def test_linkedlist_size_one_node():
    """
    Test LinkedList method size with a LinkedList with one Node (head).
    """

    llist = LinkedList()
    llist.add(10, 10)
    assert llist.size() == 1



def test_linkedlist_size_100_nodes():
    """
    Test LinkedList method with a LinkedList with 100 Nodes.
    """

    llist = LinkedList()
    for n in range(1, 101):
        llist.add(n, n)

    assert llist.size() == 100


def test_linkedlist_traverse_success_zero_nodes():
    """
    Test LinkedList method traverse's success with a LinkedList
    with zero Nodes.
    """
    
    llist = LinkedList()
    assert llist.traverse(0) == None


def test_linkedlist_traverse_failure_zero_out_of_bound():
    """
    Test LinkedList method traverse's trying to find index 1
    on a empty LinkedList.
    """

    llist = LinkedList()
    with pytest.raises(ValueError, match="Index out of bound"):
        llist.traverse(1)

def test_linkedlist_traverse_success_one_node():
    """
    Test LinkedList method traverse's success with a LinkedList
    with one Node (finding node index 1).
    """

    llist = LinkedList()
    llist.add(10, 10)

    assert llist.traverse(0) == Node(10, 10)

def test_linkedlist_traverse_failure_one_node():
    """
    Test LinkedList method traverse's trying to find index 2
    on a one Node LinkedList.
    """

    llist = LinkedList()
    llist.add(10, 10)

    with pytest.raises(ValueError, match="Index out of bound"):
        llist.traverse(2)


def test_linkedlist_traverse_success_multiple_nodes():
    """
    Test LinkedList method traverse's success with a LinkedList
    with multiple Nodes.
    """

    llist = LinkedList()
    for n in range(1, 101):
        llist.add(n, n)

    assert llist.traverse(97) == Node(3, 3)

def test_linkedlist_traverse_failure_multiple_nodes():
    """
    Test LinkedList method traverse's trying to find index 101
    on a 100 Node LinkedList.
    """

    llist = LinkedList()
    for n in range(1, 101):
        llist.add(n, n)

    with pytest.raises(ValueError, match="Index out of bound"):
        llist.traverse(101)


def test_linkedlist_repr_zero_nodes():
    """
    Test LinkedList method __repr__ in a LinkedList with zero Nodes.
    """

    llist = LinkedList()
    assert llist.__repr__() == "<Head: None>"


def test_linkedlist_repr_one_node():
    """
    Test LinkedList method __repr__ in a LinkedList with one Node.
    """

    llist = LinkedList()
    llist.add(10, 10)

    assert llist.__repr__() == "<Head: pid 10 | prio 10>"


def test_linkedlist_repr_multiple_nodes():
    """
    Test LinkedList method __repr__ in a LinkedList with multiple Nodes.
    """

    llist = LinkedList()
    llist.add(10, 10)
    llist.add(11, 11)
    llist.add(12, 12)
    llist.add(13, 13)

    assert llist.__repr__() == "<Head: pid 10 | prio 10> → <pid 11 | prio 11> → <pid 12 | prio 12> → <Tail: pid 12 | prio 12>"

