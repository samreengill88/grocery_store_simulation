"""Assignment 1 - Grocery Store Simulation

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:
This module contains some starter tests for Assignment 1.
You may add additional tests here, but you will not hand in this file.
"""
from io import StringIO
from simulation import GroceryStoreSimulation
from event import CustomerArrival, create_event_list
from store import GroceryStore, Customer, Item
from store import RegularLine, ExpressLine, SelfServeLine

CONFIG_FILE = '''{
  "regular_count": 1,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''

EVENT_FILE = '''10 Arrive Tamara Bananas 7
5 Arrive Jugo Bread 3 Cheese 3
'''


# a provided sample test for the whole simulation
def test_simulation() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
    gss.run(create_event_list(StringIO(EVENT_FILE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}


# Note: You can write additional tests here or in a separate file
# You will hand in this file. The only tests you will hand in are your tests
# for class PriorityQueue in file test_container.py.


CONFIG_FILE_2 = '''{
  "regular_count": 0,
  "express_count": 1,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''


def test_simulation_express() -> None:
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE_2))
    gss.run(create_event_list(StringIO(EVENT_FILE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}


CONFIG_FILE_3 = '''{
  "regular_count": 0,
  "express_count": 0,
  "self_serve_count": 1,
  "line_capacity": 1
}
'''


def test_simulation_self_serve() -> None:
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE_3))
    gss.run(create_event_list(StringIO(EVENT_FILE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 31, 'max_wait': 21}


CONFIG_FILE_CLOSE = '''{
  "regular_count": 2,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''

EVENT_FILE_CLOSE = '''10 Arrive Tamara Bananas 7
5 Arrive Jugo Bread 3 Cheese 3
0 Close 0
'''


def test_simulation_close() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE_CLOSE))
    gss.run(create_event_list(StringIO(EVENT_FILE_CLOSE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}


def test_enter_line2() -> None:
    config_file_name = 'input_files/config_100_10.json'
    config_file = open(config_file_name)
    s2 = GroceryStore(config_file)
    config_file.close()

    item_list = [Item('bananas', 7)]

    b1 = Customer('B1', item_list)
    b2 = Customer('B2', item_list)
    b3 = Customer('B3', item_list)
    b4 = Customer('B4', item_list)
    b5 = Customer('B5', item_list)
    b6 = Customer('B6', item_list)
    b7 = Customer('B7', item_list)
    b8 = Customer('B8', item_list)
    b9 = Customer('B9', item_list)
    b10 = Customer('B10', item_list)

    assert s2.enter_line(b1) == 0
    assert s2.enter_line(b2) == 0
    assert s2.enter_line(b3) == 0
    assert s2.enter_line(b4) == 0
    assert s2.enter_line(b5) == 0
    assert s2.enter_line(b6) == 0
    assert s2.enter_line(b7) == 0
    assert s2.enter_line(b8) == 0
    assert s2.enter_line(b9) == 0
    assert s2.enter_line(b10) == 0


def test_enter_line() -> None:
    config_file_name = 'input_files/config_333_10.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    config_file.close()

    item_list = [Item('bananas', 7)]
    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 1)
    i5 = Item('onion', 7)
    i6 = Item('tomato', 2)
    i7 = Item('ginger', 7)
    i8 = Item('pasta', 9)

    b1 = Customer('B1', item_list) # 7
    b2 = Customer('B2', [i2]) # 2
    b3 = Customer('B3', [i1, i2, i3, i4, i5, i6, i7, i8]) # 38
    b4 = Customer('B4', [i3, i4]) # 4
    b5 = Customer('B5', [i1, i2, i3, i4, i5, i6, i7, i8]) # 38
    b6 = Customer('B6', [i1, i2, i3, i4, i5, i6, i7, i8]) #38
    b7 = Customer('B7', [i8]) # 9
    b8 = Customer('B8', [i2, i3]) # 5

    assert s1.enter_line(b1) == 0
    assert s1.enter_line(b2) == 1
    assert s1.enter_line(b3) == 5
    assert s1.enter_line(b4) == 2
    assert s1.enter_line(b5) == 6
    assert s1.enter_line(b6) == 7
    assert s1.enter_line(b7) == 3
    assert s1.enter_line(b8) == 4


def test_010_10_enter_line() -> None:
    config_file_name = 'input_files/config_010_10.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    config_file.close()

    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 1)
    i5 = Item('onion', 7)
    i6 = Item('tomato', 2)
    i7 = Item('ginger', 7)
    i8 = Item('pasta', 9)

    b1 = Customer('B1', [i1])
    b2 = Customer('B2', [i2])
    b3 = Customer('B3', [i3])
    b4 = Customer('B4', [i4])
    b99 = Customer('B3', [i1, i2, i3, i4, i5, i6, i7, i8])

    assert s1.enter_line(b1) == 0
    s1.enter_line(b99)  # error
    assert s1.enter_line(b2) == 0
    assert s1.enter_line(b99)  # error
    assert s1.enter_line(b3) == 0
    assert s1.enter_line(b4)  # error


def test_next_checkout_time() -> None:
    config_file_name = 'input_files/config_111_01.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    config_file.close()

    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 1)

    c1 = Customer('c1', [i1, i2, i3, i4])
    c2 = Customer('c2', [i3])
    c3 = Customer('c3', [i1, i2])

    assert s1.enter_line(c1) == 0
    assert s1.enter_line(c2) == 1
    assert s1.enter_line(c3) == 2

    assert s1.next_checkout_time(0) == 13
    assert s1.next_checkout_time(1) == 3
    assert s1.next_checkout_time(2) == 18


def test_remove_front_customer() -> None:
    config_file_name = 'input_files/config_111_01.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    config_file.close()

    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 1)

    c1 = Customer('c1', [i1, i2, i3, i4])
    c2 = Customer('c2', [i3])
    c3 = Customer('c3', [i1, i2])
    c4 = Customer('c4', [i4])
    c5 = Customer('c5', [Item('Dates', 5), Item('Bread', 3), Item('tea', 4),
                         Item('Gum', 1)])
    c6 = Customer('c6', [i1])

    s1.enter_line(c1)
    s1.enter_line(c2)
    s1.enter_line(c3)
    s1.enter_line(c4)
    s1.enter_line(c5)
    s1.enter_line(c6)
    s1.enter_line(c1)
    s1.enter_line(c2)
    s1.enter_line(c3)

    assert s1.remove_front_customer(0) == 1
    assert s1.remove_front_customer(0) == 0

    assert s1.remove_front_customer(2) == 1


def test_line_next_checkout_time() -> None:
    reg1 = RegularLine(4)
    ser1 = SelfServeLine(3)
    exp1 = ExpressLine(3)

    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 4)

    c1 = Customer('c1', [i1, i2])
    c2 = Customer('c2', [i3, i4])
    c3 = Customer('c3', [i2])
    c4 = Customer('c4', [i1, i2, i3, i4])

    reg1.accept(c1)
    reg1.accept(c2)
    reg1.accept(c3)
    reg1.accept(c4)

    ser1.accept(c1)
    ser1.accept(c2)
    ser1.accept(c3)

    exp1.accept(c1)
    exp1.accept(c2)

    assert reg1.next_checkout_time() == 9
    assert len(reg1) == 4
    reg1.remove_front_customer()
    assert len(reg1) == 3
    assert reg1.first_in_line().name == 'c2'
    reg1.close()
    assert len(reg1) == 1
    assert reg1.first_in_line().name == 'c2'
    assert not reg1.is_open

    assert ser1.next_checkout_time() == 18
    assert exp1.next_checkout_time() == 9


def test_create_event_list() -> None:
    event_file2 = 'input_files/events_mixtures.txt'
    with open(event_file2, 'r') as event_file2:
        content = event_file2.read()
    event_file2 = StringIO(content)

    event_lst = create_event_list(event_file2)
    assert len(event_lst) == 18


def test_customer_arrival_do() -> None:
    # 333_10- 2_1_1_2

    config_file_name = 'input_files/config_333_10.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    item_list = [Item('bananas', 7)]
    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 1)
    i5 = Item('onion', 7)
    i6 = Item('tomato', 2)
    i7 = Item('ginger', 7)
    i8 = Item('pasta', 9)

    b1 = Customer('B1', item_list)
    b2 = Customer('B2', item_list)
    b3 = Customer('B3', [i1, i2, i3, i4, i5, i6, i7, i8])
    b4 = Customer('B4', item_list)
    b5 = Customer('B5', [i1, i2, i3, i4, i5, i6, i7, i8])
    b6 = Customer('B6', [i1, i2, i3, i4, i5, i6, i7, i8])
    b7 = Customer('B7', item_list)
    b8 = Customer('B8', item_list)
    s1.enter_line(b1)
    assert s1.enter_line(b2) == 1
    assert s1.enter_line(b3) == 3
    assert s1.enter_line(b4) == 2
    assert s1.enter_line(b5) == 0
    assert s1.enter_line(b6) == 1
    assert s1.enter_line(b7) == 2
    assert s1.enter_line(b8) == 3

    b9 = Customer('B9', item_list)
    e1 = CustomerArrival(5, b9)
    assert e1.do(s1)[0].timestamp == 6

def test_close_line() -> None:
    config_file_name = 'input_files/111_03.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    item_list = [Item('bananas', 7)]
    i1 = Item('bananas', 7)
    i2 = Item('cheese', 2)
    i3 = Item('mango', 3)
    i4 = Item('apple', 1)
    i5 = Item('onion', 7)
    i6 = Item('tomato', 2)
    i7 = Item('ginger', 7)
    i8 = Item('pasta', 9)

    b1 = Customer('Mia', [i1, i2, i3, i4, i5, i6, i7, i8, i1, i2, i3, i4])
    b2 = Customer('Pedro', [i1, i2, i3, i4, i5, i6, i7, i8, i1])
    b3 = Customer('Leo', [i1, i2, i3, i4, i5, i6, i7, i8, i1, i2, i3, i4, i8, i1 ])
    b4 = Customer('Jasmine', [i1, i2, i3, i4, i5, i6, i7, i8, i1, i2])
    b5 = Customer('Xin', [i1, i2, i3])
    b6 = Customer('Sadia',[i1, i2, i3, i4, i5, i6, i7, i8, i1])
    b7 = Customer('B7', item_list)
    b8 = Customer('B8', item_list)
    assert s1.enter_line(b1) == 0
    assert s1.enter_line(b2) == 2
    assert s1.enter_line(b3) == 0
    assert s1.enter_line(b4) == 2
    assert s1.enter_line(b5) == 1
    assert s1.enter_line(b6) == 0


def test_close_line_2() -> None:
    config_file_name = 'input_files/config_111_10.json'
    config_file = open(config_file_name)
    s1 = GroceryStore(config_file)
    chips = Item('Chips', 2)
    bread = Item('Bread', 3)
    raddish = Item('Raddish', 6)
    gum = Item('Gum', 1)
    bananas = Item('Bananas', 7)
    cheese = Item('Cheese', 3)
    milk = Item('Milk', 4)
    fish = Item('Fish', 15)
    meat = Item('Meat', 12)
    flowers = Item('Flowers', 22)
    lettuce = Item('Lettuce', 10)
    pop = Item('Pop', 20)
    james = Customer('James', [chips])
    wilson = Customer('Wilson', [meat, milk, flowers, lettuce])
    janice = Customer('Janice', [bread, bananas, chips, raddish])
    trevor = Customer('Trevor', [flowers, bread, cheese, cheese])
    john = Customer('John', [pop, fish, lettuce])
    jack = Customer('Jack',[gum, gum, gum, gum, gum, gum, gum, gum, gum, gum, gum])
    tara = Customer('Tara', [meat, milk, milk, lettuce])
if __name__ == '__main__':
    import pytest

    pytest.main(['test_a1.py'])
