# Node class tests

import pytest
from node import Node

def test_node_init_sucess():
    """
    Test if its possible to instantiate a Node with all correct values
    """

    node = Node(10, 10)

    assert node is not None
    assert node.pid is not None
    assert node.pid >= 1 and node.pid <= 10**9
    assert node.prio >= 0 and node.prio <= 10**5


def test_node_init_invalid_pid_max():
    """
    Test if a error is raised after a atempt to instantiate a Node with
    a value for pid greater than the maximum value.
    """

    with pytest.raises(ValueError, match="pid value is over 10\*\*9"):
        Node(10000000000, 10)


def test_node_init_invalid_pid_min():
    """
    Test if a error is raised after a atempt to instantiate a Node with
    a value for pid less than the minimum value.
    """

    with pytest.raises(ValueError, match="pid value is less than 1"):
        Node(0, 10)


def test_node_init_invalid_prio_max():
    """
    Test if a error is raised after a atempt to instantiate a Node with
    a value for prio greater than the maximum value.
    """

    with pytest.raises(ValueError, match="prio value is over 10\*\*5"):
        Node(10, 10000000000)


def test_node_init_invalid_prio_min():
    """
    Test if a error is raised after a atempt to instantiate a Node with
    a value for prio less than the mininum value.
    """

    with pytest.raises(ValueError, match="prio value is less than 0"):
        Node(10, -1)

def test_node_set_neighbor_success():
    """
    Test if the method set_neighbor correctly sets a neighbor.
    """

    n1 = Node(10, 10)
    n2 = Node(11, 20)
    try:
        n1.set_neighbor(n2)
    except TypeError as exc:
        assert False, f"n1.set_neighbor(n2) raised and exception: {exc}"

def test_node_has_neighbor_failure():
    """
    Test if the method set_neighbor raises an error if the neighbor is not
    a Node.
    """

    n1 = Node(10, 10)
    n2 = "Test"
    with pytest.raises(TypeError, match="neighbor should be of type Nod"):
        n1.set_neighbor(n2)

def test_node_has_neighbor_true():
    """
    Test if the method has_neighbor returns True if there's a neighbor
    defined.
    """

    n1 = Node(10, 10)
    n2 = Node(11, 20)
    n1.set_neighbor(n2)

    assert n1.has_neighbor() == True

def test_node_has_neighbor_false():
    """
    Test if the method has_neighbor returns False if no neighbor is
    defined.
    """

    n1 = Node(10, 10)

    assert n1.has_neighbor() == False

def test_node_eq_true():
    """
    Test a case where two nodes with same pid and prio should be
    considered equal (return True).
    """
    n1 = Node(1, 10)
    n2 = Node(1, 10)

    assert n1 == n2

def test_node_eq_false():
    """
    Test a case where two nodes with the same prio but different
    pid should be considered different (return False).
    """

    n1 = Node(1, 10)
    n2 = Node(2, 10)

    assert n1 != n2


def test_node_del_neighbor_success():
    """
    Test deletion of a existing neighbor.
    """

    # TODO
    ...

def test_node_del_neighbor_failure():
    """
    Test deletion of a non-existing neighbor.
    """

    # TODO
    ...


def test_node_repr():
    """
    Test if __repr__ is correctly defined.
    """

    node = Node(10, 10)
    assert node.__repr__() == "<Node: pid 10 | prio 10>"
