#!/usr/bin/env python
# -*- coding: utf-8 -*-


def multiply(*args):
    """Multiply and returns the products of its arguments

    :args: multipliers
    :returns: product of args

    """
    prod = 1
    for num in args:
        prod *= num
    return prod


print("multiply({}, {}) = {}".format(4, 5, multiply(4, 5)))
print("multiply({}, {}, {}) = {}".format(4, 5, 3, multiply(4, 5, 3)))


def print_kwargs(**kwargs):
    """TODO: Docstring for print_kwargs.

    :**kwargs: TODO
    :returns: TODO

    """
    print(kwargs)

print_kwargs()
print_kwargs(mean=2, sigma=2)
