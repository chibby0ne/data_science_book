#!/usr/bin/env python
# -*- coding: utf-8 -*-

height_weight_age = [70, # inches,
                    170, # pounds,
                    40 ] # years

grades = [95, # exam1
        80,   # exam2
        75,   # exam3
        62]   # exam4

def vector_add(v, w):
    """Adds corresponding elements

    :v: list representing a vector
    :w: list representing a vector
    :returns: vector sum of v and w

    """
    return [v_i + w_i for v_i, w_i in zip(v, w)]
        
def vector_substract(v, w):
    """Substracts corresponding elements

    :v: list representing a vector
    :w: list representing a vector
    :returns: vector sum of v and w as a list

    """
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """sums all corresponding elements

    :vectors: list containing all the vectors
    :returns: list containing sum of all vectors

    """
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

from functools import reduce

def vector_sum2(vectors):
    """sums all corresponding elements

    :vectors: list containing all the vectors
    :returns: list containing sum of all vectors

    """
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """c is a number, v is a vector

    :c: number
    :v: vector
    :returns: new list

    """
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """TODO: Docstring for vector_mean.

    :vectors: TODO
    :returns: TODO

    """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    """v_1 * w_1 + .... v_n * w_n

    :v: TODO
    :w: TODO
    :returns: TODO

    """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n

    :v: TODO
    :returns: TODO

    """
    return dot(v, v)

import math

def magnitude(v):
    """TODO: Docstring for magnitude.

    :v: TODO
    :returns: TODO

    """
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """TODO: Docstring for squared_distance.

    :v: TODO
    :w: TODO
    :returns: TODO

    """
    return sum_of_squares(vector_substract(v, w))


def distance(v, w):
    """TODO: Docstring for distance.

    :v: TODO
    :w: TODO
    :returns: TODO

    """
    return math.sqrt(squared_distance(v, w))


def distance2(v, w):
    """TODO: Docstring for distance.

    :v: TODO
    :w: TODO
    :returns: TODO

    """
    return magnitude(vector_substract(v, w))

#########################
# Matrices
#########################

def shape(A):
    """ return the dimensions of the matrix

    :A: matrix in list of list representation
    :returns: tuple containing rows, and columns

    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    """returns the row i of matrix A

    :A: matrix in list of list representation
    :i: row number (starts from 0)
    :returns: returns row as a list

    """
    return A[i]

def get_column(A, j):
    """TODO: Docstring for get_column.

    :A: TODO
    :j: TODO
    :returns: TODO

    """
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i, j)th entry is entry_fn(i, j)

    :num_rows: TODO
    :num_cols: TODO
    :entry_fn: TODO
    :returns: TODO

    """
    return [[entry_fn(i, j)
        for j in range(num_cols)]
        for i in range(num_rows)]


def is_diagonal(i, j):
    """1's on the diagonal 0's everwhere else

    :i: TODO
    :j: TODO
    :returns: TODO

    """
    return 1 if i == j else 0


vector_a = [1, 2, 1]
print("vector_a: " + str(vector_a))
vector_b = [1, 2, 1]
print("vector_b: " + str(vector_b))
vector_c = [2, 1, 2]
print("vector_c: " + str(vector_c))

vector_sum_a_b = vector_add(vector_a, vector_b)
print("vector_add(vector_a, vector_b): " + str(vector_sum_a_b))
vector_sub_a_b = vector_substract(vector_a, vector_b)
print("vector_substract(vector_a, vector_b): " + str(vector_sub_a_b))

vector_all = [vector_a, vector_b, vector_c] 
print("vector_sum: " + str(vector_all))
print("vector_sum(vector_all) : " + str(vector_sum(vector_all)))

print(vector_sum2(vector_all))
print("vector_sum2(vector_all) : " + str(vector_sum(vector_all)))

print("scalar_multiply(5, vector_a): " + str(scalar_multiply(5, vector_a)))

print("vector_mean(vector_all): " + str(vector_mean(vector_all)))
print("dot(vector_a, vector_b): " + str(dot(vector_a, vector_b)))

print("sum_of_squares(vector_a): " + str(sum_of_squares(vector_a)))

print("magnitude(vector_a): " + str(magnitude(vector_a)))

print("squared_distance(vector_a, vector_b): " + str(squared_distance(vector_a, vector_b)))
print("squared_distance(vector_a, vector_c): " + str(squared_distance(vector_a, vector_c)))

print("distance(vector_a, vector_b): " + str(distance(vector_a, vector_b)))
print("distance(vector_a, vector_c): " + str(distance(vector_a, vector_c)))

#########################
# Matrices
#########################

A = [[1, 2, 3],
        [4, 5, 6]]

B = [[1, 2],
        [3, 4],
        [5, 6]]

print("A: " + str(A))
print("B: " + str(B))

print("shape(A): " + str(shape(A)))

print("get_row(A, 1): " + str(get_row(A, 1)))
print("get_column(A, 1): " + str(get_column(A, 1)))


identity_matrix = make_matrix(5, 5, is_diagonal)
print("identity matrix 5 x 5: "  + str(identity_matrix))
