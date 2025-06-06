class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        res = 0
        l = 0
        for i in range(len(s)):
            while s[i] in res_set:
                res_set.remove(s[l])
                l += 1
            res_set.add(s[i])
            res = max(res, i-l+1)
        return res


"""
3. Longest Substring Without Repeating Characters

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""