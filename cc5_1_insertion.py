#!/usr/bin/env python3.5

"""
Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i 
and j. Write a method to insert Minto N such that M starts at bit j and ends 
at bit i. You can assume that the bits j through i have enough space to fit 
all of M. That is, if M = 10011, you can assume that there are at least 5 bits 
between j and i. You would not, for example, have j = 3 and i = 2, because M 
could not fully fit between bit 3 and bit 2.
"""


#Text space:
#
#num = 1011010101101001101
#new = 01011
#i = 7
#j = 13 (= i + len(new))
#
#    1011010101101001101
#AND 1111111000001111111
#          j    i
#
#    1011010000001001101
#OR  0000000010110000000
#
#    1011010010111001101
#
#
#Code space:

def insert(new, num, j, i):
    if (
        not isinstance(new, int) or
        not isinstance(num, int) or
        not isinstance(j, int) or
        not isinstance(i, int)
    ):
        raise TypeError("Input arguments must be int")
    N = num.bit_length()
    mask = (2**N) - 1
    augmentor = (1 << q)
    for q in range(i, j):
        mask = revert(mask & augmentor)
        augmentor = augmentor << 1
    
    num = num & augmentor
    num = num | new
    return num

def revert(a):
    N = a.bit_length()
    return (2**N - 1) - a

class TestInsert():
    def test_insert_normal(self):
        num = int('1011010101101001101', 2)
        new = int('01011', 2)
        i = 7
        j = 13
        expected = '1011010010111001101'
        assert insert(new, num, j, i) == expected

    def test_invalid_input(self):
        pytest.raises(TypeError):
            insert(None, 10, 2, 1)

