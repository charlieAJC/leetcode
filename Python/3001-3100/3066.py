import heapq


class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        heapq.heapify(nums)
        while nums and nums[0] < k:
            min1 = heapq.heappop(nums)
            if not nums:
                break
            min2 = heapq.heappop(nums)
            heapq.heappush(nums, min1 * 2 + min2)
            res += 1
        return res


# nums = [2, 11, 10, 1, 3]
# k = 10
# Output: 2

nums = [1, 1, 2, 4, 9]
k = 20
# # Output: 4

print(Solution().minOperations(nums, k))
