"""
Problem: Anagram
Source: GfG 160
Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/anagram-1587115620

Time Complexity: O(n)
Space Complexity: O(k)
"""

from typing import Dict

class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq : Dict[str, int] = {}
        for i in range(len(s1)) :
            freq[s1[i]] = freq.get(s1[i] , 0) +1
            freq[s2[i]] = freq.get(s2[i] , 0) -1

        result = all(val == 0 for val in freq.values())
        return result