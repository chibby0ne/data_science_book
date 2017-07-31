#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from collections import Counter

def make_simple_line_chart(plt):
    """Makes a simple line chart

    :plt: pyplot object

    """
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    
    # create a line chart, years on x-axis, gdp on y-axis
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    
    # add a title
    plt.title("Nominal GDP")
    
    # add a label to the y-axis
    plt.ylabel("Billions of $")
    plt.show()   

def make_simple_bar_chart(plt):
    """ Make simple bar chart

    Bar Chart is a good choice when you want to show how some quantity varies
    among some discrete sets of items

    :plt: pyplot object

    """
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    
    # Bars are by default width 0.8 so we'll add 0.1 to the elft coordinates so
    # that each bar is centered
    margin = 0
    xs = [i + margin for i, _ in enumerate(movies)]
    
    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.bar(xs, num_oscars)
    plt.bar
    
    plt.ylabel("# of Academy Awards")
    plt.xlabel("My Favorite Movies")
    
    # label x-axis with movie names at bar centers
    margin = 0
    plt.xticks([i + margin for i, _ in enumerate(movies)], movies)
    
    plt.show()

def make_histogram_graph(plt):
    """ Makes a histogram graph

    A bar chart can also be a good choice for plotting histograms of bucketed
    numeric values, in order to visualize how the values are distributed

    :plt: pyplot object
    """
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    # floor division so that every grade is in buckets of 10
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)
    
    plt.bar([x - 0 for x in histogram.keys()],   # shift each bar to the left by 4
            histogram.values(),                 # give each bar its correct height
            8)                                  # give each bar a width of 8
    
    plt.axis([-5, 105,                          # x-axis from -5 to 105
            0, 5])                              # y-axis from 0 to 5
                                               
    plt.xticks([10 * i for i in range(11)])     # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()

def make_bar_graph_misleading_y_axis(plt, misleading=False):
    """Plots a bar graph using a y-axis range that depends on the value of the
    milesading parameter

    You can make the bar chart misleading by having the wrong values for the
    y-axis.  
    You can fix this by setting the y values to a sensible range that
    would more accuratly represent the values you're graphing

    :plt: plt object
    :misleading: True to make y-axis of graph misleading, false otherwise
    """
    mentions = [500, 505]
    years = [2013, 2014]

    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")

    # if you don't do this, matplotlib will albel the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    plt.ticklabel_format(useOffset=False)

    # misleading y-axis only shows the part above 500
    if misleading:
        plt.axis([2012.5, 2014.5, 499, 506])
    else:
        plt.axis([2012.5, 2014.5, 0, 550])
    plt.title("Look at the 'Huge' Increase!")
    plt.show()

def make_line_chart_trend(plt):
    """ Creates a line chart that exposes a trend

    Line Charts are a good choice for showing trends

    :plt: pyplot object

    """
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    # we can make multiple calls to plt.plot
    # to show multiple series on the same chart
    plt.plot(xs, variance, "g-", label="variance")          # green solid line
    plt.plot(xs, bias_squared, "r-.", label="bias_squared") # red dot-dashed line
    plt.plot(xs, total_error, "b:", label="total_error")     # blue dotted line

    # because we've assigned labels to each series
    # we can get a legend for free
    # loc=9 means 'top center'

    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()

def make_scatterplot_chart(plt):
    """Makes a scatterplot chart. 

    Scatterplot is the right choice for visualizing the relationship between
    two paired sets of data

    :plt: pyplot object

    """
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                xy = (friend_count, minute_count),  # put the label wit its point
                xytext = (5, -5),                   # but slightly offset
                textcoords = "offset points")
    plt.title("Daily Minutes vs. Number of Friends")        
    plt.xlabel("# of friends")
    plt.ylabel("Daily minutes spent on the site")
    plt.show()


def make_scatterplot_misleading_chart(plt, misleading=False):
    """Makes a scatterplot chart

    If you're scatteting comparable variables, you might get a misleading
    picture if you let matplotlib choose the scale.
    You can fix this by doing a call to plt.axis("equal"), which sets both axis
    scales to equal values

    :plt: pyplot object
    :misleading: True to make graph misleading, false otherwise

    """
    test_1_grades = [99, 90,  85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)
    plt.title("Axes Aren't Comparable")
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")
    if misleading == False:
        plt.axis("equal")
    plt.show()

make_simple_line_chart(plt)
make_simple_bar_chart(plt)
make_histogram_graph(plt)
make_bar_graph_misleading_y_axis(plt, True)
make_bar_graph_misleading_y_axis(plt)
make_line_chart_trend(plt)
make_scatterplot_chart(plt)
make_scatterplot_misleading_chart(plt, True)
make_scatterplot_misleading_chart(plt)
