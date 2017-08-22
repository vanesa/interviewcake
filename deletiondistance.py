#!/usr/bin/python

"""
PRAMP
Deletion Distance

The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer
"""

import unittest

def deletion_distance(str1, str2):
  
  if str1 == str2:
    return 0
  
  if not str1:
    return len(str2)
  
  if not str2:
    return len(str1)
  
  newstr1 = ''
  count = 0
  for i, c in enumerate(str1):
    i2=str2.find(c)
    if i2 != -1:
      newstr1 += c
      str2 = str2[:i2] + str2[i2+1:]
    else:
      count += 1
  
  str2len = len(str2)
  totalcount = str2len + count
  
  return totalcount

class Test(unittest.TestCase):
  data = [(
      ["asdfzzd","asdfwre"], 6
    ),(
      ["some","some"], 0
    ), (
      ["some", "thing"], 9
    ), (
      ["", ""], 0
    ), (
      ["", "hey"], 3
    )
  ]

  def test_deletion_distance(self):
    for [[str1, str2], expected] in self.data:
      actual = deletion_distance(str1, str2)
      self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()

