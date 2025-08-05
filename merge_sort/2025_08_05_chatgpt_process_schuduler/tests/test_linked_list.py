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

    with pytest.raises(ValueError, match="pid value is over 10**9"):
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

    # TODO
    ...

def test_linkedlist_size_zero_node():
    """
    Test LinkedList method size with a empty LinkedList.
    """

    # TODO
    ...

def test_linkedlist_size_one_node():
    """
    Test LinkedList method size with a LinkedList with one Node (head).
    """

    # TODO
    ...

def test_linkedlist_size_100_nodes():
    """
    Test LinkedList method with a LinkedList with 100 Nodes.
    """

    # TODO
    ...

def test_linkedlist_traverse_success_zero_nodes():
    """
    Test LinkedList method traverse's success with a LinkedList
    with zero Nodes.
    """

    # TODO
    ...

def test_linkedlist_traverse_failure_zero_nodes():
    """
    Test LinkedList method traverse's failure with a LinkedList
    with zero Node.
    """

    # TODO
    ...

def test_linkedlist_traverse_success_one_node():
    """
    Test LinkedList method traverse's success with a LinkedList
    with one Node.
    """

    # TODO
    ...

def test_linkedlist_traverse_failure_one_node():
    """
    Test LinkedList method traverse's failure with a LinkedList
    with one Node.
    """

    # TODO
    ...


def test_linkedlist_traverse_success_multiple_nodes():
    """
    Test LinkedList method traverse's success with a LinkedList
    with multiple Nodes.
    """

    # TODO
    ...

def test_linkedlist_traverse_failure_multiple_nodes():
    """
    Test LinkedList method traverse's failure with a LinkedList
    with multiple Nodes.
    """

    # TODO
    ...


def test_linkedlist_repr_zero_nodes():
    """
    Test LinkedList method __repr__ in a LinkedList with zero Nodes.
    """

    # TODO
    ...

def test_linkedlist_repr_one_node():
    """
    Test LinkedList method __repr__ in a LinkedList with one Node.
    """

    # TODO
    ...

def test_linkedlist_repr_multiple_nodes():
    """
    Test LinkedList method __repr__ in a LinkedList with multiple Nodes.
    """

    # TODO
    ...
