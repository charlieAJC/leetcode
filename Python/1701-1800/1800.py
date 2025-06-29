class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum


# nums = [10, 20, 30, 5, 10, 50]
# nums = [10, 20, 30, 40, 50]
nums = [12, 17, 15, 13, 10, 11, 12]
print(Solution().maxAscendingSum(nums))
