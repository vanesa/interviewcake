#!usr/bin/evn python
# -*- coding: utf-8 -*-

"""
PRAMP

Award Budget Cuts

The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

Example:

input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
Constraints:

[time limit] 5000ms

[input] array.double grantsArray

0 ≤ grantsArray.length ≤ 20
0 ≤ grantsArray[i]
[input] double newBudget

[output] double

"""

import unittest

def find_grants_cap(grantsArray, newBudget):
  
  grantsArray.sort(reverse=True)
  
  for i, g in enumerate(grantsArray):
    
    if newBudget <=g:
      continue

    if newBudget > g and newBudget > sum(grantsArray[i:]):
      av = (float(newBudget) - sum(grantsArray[i:]))/i

      if av < g and i == len(grantsArray)-1:
        av = float(newBudget)/len(grantsArray)
        return av

      if av < g and i != len(grantsArray)-1:
        continue

      if av > g and i != len(grantsArray)-1:
        return av

      if av > g and i == len(grantsArray)-1:
        return av

class Test(unittest.TestCase):
  data = [(
    [[2,4], 3], 1.5
    ),(
    [[2,4,6], 3], 1.0
    ),(
    [[2,100,50,120,167], 400], 128.0
    ),(
    [[2,100,50,120,1000], 190], 47.0
    ),(
    [[21,100,50,120,130,110], 140], 23.8
    ),(
    [[210,200,150,193,130,110,209,342,117], 1530], 211.0
    )]

  def test_find_grants_cap(self):

    for [[case, budget], expected] in self.data:
      actual = find_grants_cap(case, budget)
      self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()