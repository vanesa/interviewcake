#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PRAMP

Sales Path

The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). 
The root is the company itself, and every node in the tree represents a car distributor that receives cars 
from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell 
cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

            0
          / |  \
        5   3   6
      /   /  \  / \
    4   2    0  1   5
      /     /
    1      10
   / 
  1

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, 
is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. 
For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write an 
function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost 
is 7: 0→6→1 and 0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer
"""

import sys
import random

def get_cheapest_cost(rootNode):
  
  if not rootNode.children:
    # print 'Node(' + str(rootNode.cost) + ') min_cost=' + str(rootNode.cost)
    return rootNode.cost
  
  min_cost=sys.maxsize
  for child in rootNode.children:
    path_cost = get_cheapest_cost(child)
    if path_cost < min_cost:
      min_cost = path_cost
      
  # print 'Node(' + str(rootNode.cost) + ') min_cost=' + str(min_cost + rootNode.cost)
  
  return min_cost + rootNode.cost

class Node:

  def __init__(self, cost, children=[]):
    self.cost = cost
    self.children = children
    self.parent = None
    for child in self.children:
      child.parent = self

  def __repr__(self):
    return str(self.cost)

def createTree(maxdepth=30, currentdepth=0):
  cost = random.randint(0, 9)
  children = []
  if currentdepth < maxdepth and random.randint(0, 1):
    x = random.randint(0, 3)
    for num in xrange(x):
      children.append(createTree(maxdepth=maxdepth, currentdepth=currentdepth+1))

  print cost
  return Node(cost, children=children)


# rootNode = Node(0, children=[
#   Node(5, children=[
#     Node(4),
#     ]),
#   Node(3, children=[
#     Node(2, children=[
#       Node(1, children=[
#         Node(1),
#       ]),
#     ]),
#     Node(0, children=[
#       Node(10),
#     ])
#   ]), 
#   Node(6, children=[
#     Node(1), 
#     Node(5),
#   ]),
# ])



if __name__ == '__main__':
  rootNode = createTree()
  print 'cheapest: ', get_cheapest_cost(rootNode)