# Given an integer array and a number k, output all pairs that sum up to k. 

# [5, 6, 1, 2, 9, 0, 3, 4] k = 5

# (5, 0) (2, 3) (1, 4)

import unittest

def findpairs(array, k):
    
    tracker = {}
    result = []
    
    for i, n in enumerate(array):

        if n * 2 == k:
            result.append((n, n))
            continue
        
        n2 = k - n
        
        if n in tracker.keys():
            
            for i2 in tracker[n]:
                result.append((array[i2], n))
        
        if n2 in tracker.keys():
            tracker[n2].append(i)
            continue
        
        tracker[n2] = [i]
        
    return result

class Test(unittest.TestCase):
    data = [(
        [[5, 6, 1, 2, 9, 0, 3, 4], 5], 
        [(5, 0),(2, 3),(1, 4)]
        ),
    (
        [[1, 6, 9, 5, 3, 6, 4, 8, 0, 2, 2, 4], 6], 
        [(1, 5), (3, 3), (6, 0), (6, 0), (4, 2), (4, 2), (2, 4), (2, 4)]
        )
    ]

    def test_findpairs(self):
        for [[array, num], expected] in self.data:
            actual = findpairs(array, num)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
