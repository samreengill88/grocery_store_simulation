"""Assignment 1 - Tests for class PriorityQueue  (Task 3a)

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:
This module will contain tests for class PriorityQueue.
"""
from container import PriorityQueue


def test_add() -> None:
    """Tests add method in PriorityQueue.
    """
    pq = PriorityQueue()
    pq.add(20)
    pq.add(10)
    pq.add(30)
    pq.add(20)
    pq.add(70)

    assert pq._items == [10, 20, 20, 30, 70]
    pq.add(20)
    assert pq._items == [10, 20, 20, 20, 30, 70]
    pq.add(25)
    assert pq._items == [10, 20, 20, 20, 25, 30, 70]
    assert pq.remove() == 10
    assert not pq.is_empty()

    pq2 = PriorityQueue()
    pq2.add('a')
    pq2.add('A')
    pq2.add('b')
    pq2.add('B')
    assert pq2.remove() == 'A'

    item_removed = pq2.remove()
    type_of_item = type(item_removed)

    for item in pq2._items:
        assert isinstance(item, type_of_item)

    assert not pq2.is_empty()
    pq = PriorityQueue()
    pq.add([1, 2, 3])
    pq.add([1, 2, 3])
    assert pq._items == [[1, 2, 3], [1, 2, 3]]
    assert id(pq._items[0]) == id(pq.remove())
    assert id(pq._items[0]) == id(pq.remove())
    assert pq.is_empty()


if __name__ == '__main__':
    import pytest

    pytest.main(['test_priority_queue.py'])
