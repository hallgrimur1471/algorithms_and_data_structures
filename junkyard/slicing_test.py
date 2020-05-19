#!/usr/bin/env python3.5


def f(v):
    v.pop()


v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4, 5]

f(v1)
f(v2[0:5])

print(v1)
print(v2)
print(id(v1))
print(id(v2))
print(id(v2[:]))
print(id(v2[0:5]))
print(id(v2[0:4]))


def g(v):
    if v:
        print("b", id(v))
        g(v[0 : len(v) - 1])
        print("a", id(v))


print("g")
v = [1, 2, 3, 4, 5]
print(id(v))
g(v)

print("a, b")
a = "one"
print(id(a))
b = "two"
print(id(b))


def enhance(v):
    v.pop()


print("enhance")
v = [1, 2, 3, 4, 5]
v_cp = v[0 : len(v)]
enhance(v_cp)
print(v)
print(v_cp)
v_cp2 = v[0 : len(v)]
enhance(v_cp2)
enhance(v_cp2)
print(v)
print(v_cp)
print(v_cp2)
