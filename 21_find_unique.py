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
	return tracker

