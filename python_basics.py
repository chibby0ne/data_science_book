#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("all([True, 1, { 3 }] = " + str(all([True, 1, { 3 }])))
print("all([True, 1, { }]) = " + str(all([True, 1, { }])))
print("any([True, 1, { }]) = " + str(any([True, 1, { }])))
print("any([True, 0, { }]) = " + str(any([True, 0, { }])))
print("any([True]) = " + str(any([True])))
print("any([True, False]) = " + str(any([True, False])))
print("all([True, False]) = " + str(all([True, False])))
print("all([]) = " + str(all([ ])))
print("any([]) = " + str(any([ ])))
