"""
Problem: Second Largest
Source: GfG 160
Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def getSecondLargest(self, arr):
        largest = float("-inf")
        second_largest  = float("-inf")
        for i in range(len(arr)):
            if arr[i] > largest :
                second_largest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > second_largest :
                second_largest = arr[i]
        if second_largest == float("-inf") :
            return -1
        else :
            return second_largest
        