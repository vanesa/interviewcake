# Given an integer array and a number k, output all pairs that sum up to k. 

# [5, 6, 1, 2, 9, 0, 3, 4] k = 5

# (5, 0) (2, 3) (1, 4)

def findpairs(array, k):
    
    tracker = {}
    
    for i, n in enumerate(array):
        if n * 2 == k:
            print n, n

        if n in tracker.keys():
            i2 = tracker[n]
            
            print array[i2], n

        n2 = k - n
        tracker[n2] = i
        

findpairs([5, 6, 1, 2, 9, 0, 3, 4], 5)
