#!/usr/bin/env python3.5

def remove_value_at_index_i_from_list_in_constant_time(list_, i):
    tmp = list_[i]
    list_[i] = list_[-1]
    list_[-1] = tmp
    list_.pop()

list_ = ["a", "c", "e", "g", "b", "d", "t"]
remove_value_at_index_i_from_list_in_constant_time(list_, 2)
print(list_)
