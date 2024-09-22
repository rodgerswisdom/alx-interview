#!/usr/bin/python3
"""minimum time time to write operations of copy and paste"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    """loop for n number of times"""
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
