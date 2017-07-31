#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from matplotlib import pyplot as plt
from linear_algebra import sum_of_squares, dot
import math

num_friends = [100, 49, 41, 40, 25 ] 
daily_minutes = [20, 10, 5, 4, 15 ] 

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
# plt.show()


num_points = len(num_friends)
print(num_points)
largest_value = max(num_friends)
print(largest_value)
smallest_value = min(num_friends)
print(smallest_value)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

#################
#
# Central Tendencies
#
#################

# 
#
def mean(x):
    """TODO: Docstring for mean.

    :x: TODO
    :returns: TODO

    """
    return sum(x) / len(x)

print(mean(num_friends))


# The mean is too supceptible to outliers, and if we are sure that outliers are
# just bad data then the mean is a better measure of the central tendency
def median(v):
    """TODO: Docstring for function.

    :arg1: TODO
    :returns: TODO

    """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(median(num_friends))


# Is a generalization of median
# Represents the value less than which a certain percentile of the data lies
def quantile(x, p):
    """returns the pth-percentile value in x

    :x: list
    :p: percentile value
    :returns: TODO

    """
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)


# Most common value
def mode(x):
    """returns a list, wmight be more than a node

    :x: list of input
    :returns: TODO

    """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

mode(num_friends)


#########################################
#
# Dispersion - how spread out is the data
#
########################################

# "range" already means something in Python, so we'll use a different name
# range is just the difference between the largest and the smallest value
# A very simple measure of dispersion is just the difference between the largest and smallest elements
def data_range(x):
    """TODO: Docstring for data_range.

    :x: TODO
    :returns: TODO

    """
    return max(x) - min(x)

data_range(num_friends)


# A more complex measure of dispersion is the variance 

def de_mean(x):
    """translate x by substracting its mean (so the result has mean 0)

    :x: list
    :returns: 

    """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements

    :x: list
    :returns: variance integer

    """
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

variance(num_friends)


# Note that whatever units our data is in, all of our measures of central tendency are in the same unit.
# The reange will similarly be in the same unit.
# The variance on the other hand has units that are the squares of the original units
def standard_deviation(x):
    """TODO: Docstring for standard_deviation.

    :x: list
    :returns: integer 

    """
    return math.sqrt(variance(x))

standard_deviation(num_friends)


# Both the range and the mean have the same outlier problem that we saw earlier with the mean.
# A more robust alternative computes the difference between the 75th percentile value and the 25th percentile value:
# Which is quite plainly unaffected by a small number of outliers
def interquartile_range(x):
    """TODO: Docstring for interquartile_range.

    :x: TODO
    :returns: TODO

    """
    return quantile(x, 0.75) - quantile(x, 0.25)


#################################
#
# Correlation - relation of one thing with another
#
#################################

# The paired analoge of variance.
# Whereas variance measure how a single variable deviates from its mean,
# Covariance measures how to variables vary in tandem from their means
def covariance(x, y):
    """ x and y should have the same length

    :x: first variable (list)
    :y: second variable (list)
    :returns: integer

    """
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

# dot sums up the products of corresponding pairs of elements
# when corresponding elements of x and y are either both above their means or both below their means, a positive number enters the sum
# Whe one is above its mean and the other below, a negative number enters the sum.
# Correspondingly, a large positive covariance means that x tends to be large when y is larger and small when y is small.
# Correspondingly, a large negative covariance means that x tends to be large when y is small and small when y is large.
# A covariance close to zero means that no such relationship exists
print(covariance(num_friends, daily_minutes))

# It can b ehard to interpret the covariance for a copuple of reasons
# 1. Its units are the products of the inputs unitns which can be hard to make sense of.
# 2. If each user had twice as many friends (but the same number of minutes), the covariance would be twice as large.
# But in a sense the variables would be just as interrelated. Said differently, it's hard to say what counts as a "large" covariance

def correlation(x, y):
    """Calculates the correlation between two variables

    :x: list
    :y: list
    :returns: 

    """
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

print(correlation(num_friends, daily_minutes))
