# Time : O(n)
# Space: O(1)
# 128. Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        currentStreak, longestStreak = 0,0
        for i in nums_set:
            tmp = i
            if (i - 1) in nums_set:
                continue
            else:
                currentStreak = 1
                while (tmp + 1) in nums_set:
                    currentStreak += 1
                    tmp += 1
                longestStreak = max(currentStreak, longestStreak)
        return longestStreak