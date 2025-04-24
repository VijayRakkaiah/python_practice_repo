class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_pointer = 0
        right_pointer = len(nums)-1

        while left_pointer <= right_pointer:

            middle_pointer = (left_pointer + right_pointer) // 2

            if target == nums[middle_pointer]:
                return middle_pointer
            elif target > nums[middle_pointer]:
                left_pointer = middle_pointer + 1
            elif target < nums[middle_pointer]:
                right_pointer = middle_pointer - 1
        else:
            return -1


"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""