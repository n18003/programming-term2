#!/usr/bin/env python3


"""(docstring)
"""


def multiplication_table():
    """(docstring)
    """
    for i in range(1, 10):
        for j in range(1, 10):
            print('{:3}'.format(i*j), end='')
        print('')


if __name__ == '__main__':
    multiplication_table()
