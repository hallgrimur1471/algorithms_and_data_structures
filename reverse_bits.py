#!/usr/bin/env python3.5

def reverse_bits(n):
    N = n.bit_length()
    print(N)
    new = n
    clear_mask = (2**N - 1) - 1
    read_mask = 1 << (N-1)
    for i in range(N):
        clear_mask = (2**N - 1) - 2**i
        b = int((n & read_mask) != 0)
        new = new & clear_mask
        b = b << i
        new = new | b
        read_mask = read_mask >> 1
        clear_mask = clear_mask << 1
    return new

n = 43261596
print(bin(n))
print(bin(reverse_bits(n)))
