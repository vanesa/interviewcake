#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
PRAMP

Number of Paths

You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an
nxn grid. The car is supposed to get to the opposite, Northeast (top-right), corner of the grid.
Given n, the size of the grid’s axes, write a function numOfPathsToDest that returns the number 
of the possible paths the driverless car can take.

alt the car may move only in the white squares

For convenience, let’s represent every square in the grid as a pair (i,j). The first coordinate in the 
pair denotes the east-to-west axis, and the second coordinate denotes the south-to-north axis. 
The initial state of the car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal border. In other words, in 
every step the position (i,j) needs to maintain i >= j. See the illustration above for n = 5. In every 
step, it may go one square North (up), or one square East (right), but not both. E.g. if the car is at 
(3,1), it may go to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space complexities.

Example:

input:  n = 4

output: 5 # since there are five possibilities:
          # “EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”,
          # where the 'E' character stands for moving one step
          # East, and the 'N' character stands for moving one step
          # North (so, for instance, the path sequence “EEENNN”
          # stands for the following steps that the car took:
          # East, East, East, North, North, North)
Constraints:

[time limit] 5000ms

[input] integer n

1 ≤ n ≤ 100
[output] integer
"""

import unittest

def num_of_paths_to_dest(n):

  if n <= 1:
    return 1

  i = j = n - 1

  paths = get_paths(i, j)

  return paths
  
def get_paths(i, j):

  if i == 1 and j == 0:
    return 1

  if i > j and i != 0 and j != 0:
    return get_paths(i - 1, j) + get_paths(i, j - 1)

  if i != 0 and i == j:
    return get_paths(i, j - 1) 

  if j == 0:
    return get_paths(i - 1, j)
       
class Test(unittest.TestCase):
  data = [(4, 5), (1, 1), (5, 6), (0, 1)]

  def test_num_of_paths_to_dest(self):
    for [case, expected] in self.data:
      actual = num_of_paths_to_dest(case)
      self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()
