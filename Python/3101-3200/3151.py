class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # version 1
        # if len(nums) == 1:
        #     return True

        # for i in range(1, len(nums)):
        #     if (nums[i] + nums[i - 1]) % 2 != 1:
        #         return False
        # return True

        # version 2 (improved by ChatGPT)
        return all((nums[i] + nums[i - 1]) % 2 == 1 for i in range(1, len(nums)))


# nums = [1]
# nums = [2, 1, 4]
nums = [4, 3, 1, 6]
print(Solution().isArraySpecial(nums))
