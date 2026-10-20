"""
Problem: Move All Zeroes to End
Source: GfG 160
Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def pushZerosToEnd(self, arr: list[int]) -> None:
        index = 0
        for i in range(len(arr)):
            if arr[i] != 0 :
                arr[index], arr[i] = arr[i] , arr[index]
                index += 1