#!/usr/bin/python3
'''
Minimum Operations

Calculates the fewest number of operations
needed to result in n H characters in a file
'''


def minOperations(n):
    '''
    Calculates the minimum number of operations
    needed to result in n H characters in a file
    '''
    count = 0
    i = 2
    if n <= 1:
        return 0
    while n > 1:
        if n % i == 0:
            count += i
            n /= i
        else:
            i += 1
    return count
