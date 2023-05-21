#!/usr/bin/env python3

def print_fibonacci(length):
    FibArray  = [0, 1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        count = 1
        for i in range(length - 2):
            FibArray.append(count + FibArray[i])
            count = count + FibArray[i]
        print(FibArray)
