"""
26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

from typing import List


class RemoveDuplicates:
    def remove_duplicates(self, nums: List[int]) -> int:
        size = len(nums)
        k = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[k] = nums[i]
                k = k + 1
        return k