class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        mask = 0
        left = 0
        max_len = 0

        for right in range(len(nums)):
            while mask & nums[right] != 0:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len


# nums = [1, 3, 8, 48, 10]
nums = [3, 1, 5, 11, 13]
print(Solution().longestNiceSubarray(nums))
