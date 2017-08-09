"""
Interview Cake

find-unique-int-among-duplicates #21
"""
import unittest

def find_unique(drones):
	tracker = set()

	for drone in drones:
		if drone in tracker:
			tracker.remove(drone)
		else:
			tracker.add(drone)
	return list(tracker)


class Test(unittest.TestCase):
	data = [([5,1,3,4,6,2,7,8,9,2,4,5,7,8,3,6,9], [1])]

	def test_find_unique(self):
		for [case, expected] in self.data:
			actual = find_unique(case)
			self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main()