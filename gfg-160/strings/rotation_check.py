"""
Problem: String Rotation Check
Source: GfG 160
Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/check-if-strings-are-rotations-of-each-other-or-not-1587115620

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def areRotations(self, s1, s2):
        doubled_rotated = s2 + s2
        if s1 in doubled_rotated :
            return True
        else :
            return False