# 1300. Sum of Mutated Array Closest to Target
# Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

# In case of a tie, return the minimum such integer.

# Notice that the answer is not neccesarilly a number from arr.

#  

# Example 1:

# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
# Example 2:

# Input: arr = [2,3,5], target = 10
# Output: 5
# Example 3:

# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
#  

# Constraints:

# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5
import bisect
class Solution:
    def findBestValue(self, arr, target):
        res, diff = 0, target
        arr.sort()
        prefix = [0]
        for i in range(0,len(arr)):
            prefix.append(prefix[-1] + arr[i] )
        for num in range(1, arr[-1]+1):
            i = bisect.bisect_left(arr, num)
            total_sum = (len(arr) - i) * num + prefix[i]
            # print(f'num = {num}, total_sum:{total_sum}')
            if abs(target - total_sum) < diff:
                # print(f'diff = {diff}, target - total_sum = {(target - total_sum)}')
                diff = abs(target - total_sum)
                res = num
        return res

if __name__ == '__main__':
    test = Solution()
    testList = [3,2,5]
    res = test.findBestValue(testList, 10)
    print(res)