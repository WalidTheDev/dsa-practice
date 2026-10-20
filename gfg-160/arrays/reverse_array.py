"""
Problem: Move All Zeroes to End
Source: GfG 160
Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        floor_half = n//2
        for i in range(floor_half):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]