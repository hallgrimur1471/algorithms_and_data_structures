#!/usr/bin/env python3.5

"""
Given two (singly) linked lists, determine if the two lists intersect. Return
the intersecting node. Note that the intersetion is defined base on reference,
not value. This is, if the kth node of the first linked list is the exact same
node (by reference) as the jth node of the second linked list, then they are
intersecting.
"""

class SinglyLinkedList():
    def __init__(self):
        self.next_ = None

    def append(self, node):
        selection = self.next_
        if selection == None:
            self.next_ = node
            return
        while selection.next_ != None:
            selection = selection.next_
        selection.next_ = node

    def pop(self):
        if self.next_ == None:
            raise IndexError("pop from empty list")
        selection = self.next_
        last = None
        while selection.next_ != None:
            last = selection
            selection = selection.next_
        last.next_ = None
        return selection

class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

def intersect(a, b):
    a = a.next_
    b = b.next_
    a_hashset = set()
    b_hashset = set()
    while a != None or b != None:
        if a != None:
            if id(a) in b_hashset:
                return True
            a_hashset.add(id(a))
            a = a.next_
        if b != None:
            if id(b) in a_hashset:
                return True
            b_hashset.add(id(b))
            b = b.next_
    return False

def sll_test():
    s = SinglyLinkedList()
    s.append(Node(1))
    s.append(Node(2))
    s.append(Node(3))
    print("popped:", s.pop().value)
    s.append(Node(4))
    print("list:")
    selection = s.next_
    while selection != None:
        print(selection.value)
        selection = selection.next_

if __name__ == "__main__":
    a = SinglyLinkedList()
    a.append(Node(1))
    b = SinglyLinkedList()
    b.append(Node(1))
    print(intersect(a, b))

    z = Node(10)
    z.next_ = Node(11)
    a = SinglyLinkedList()
    a.append(Node(1))
    a.append(z)
    b = SinglyLinkedList()
    b.append(Node(3))
    b.append(Node(4))
    b.append(Node(5))
    b.append(z)
    print(intersect(a, b))

    z = Node(10)
    z.next_ = Node(11)
    a = SinglyLinkedList()
    a.append(z)
    b = SinglyLinkedList()
    b.append(Node(3))
    b.append(Node(4))
    b.append(Node(5))
    b.append(z)
    print(intersect(a, b))

    a = SinglyLinkedList()
    b = SinglyLinkedList()
    print(intersect(a, b))

########################################
#    def pop_old(self):
#        selection = self.next_
#        if selection == None:
#            raise IndexError("pop from empty list")
#        if selection.next_ == None:
#            self.next_ = None
#            return selection
#        while selection.next_.next_ != None:
#            selection = selection.next_
#        to_return = selection.next_
#        selection.next_ = None
#        return to_return
