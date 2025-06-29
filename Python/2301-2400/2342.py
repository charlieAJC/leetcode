import heapq
from collections import defaultdict


class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digi_count = defaultdict(list)

        # 將數字按照各位數字和分組
        for num in nums:
            # 計算各位數字和
            s = 0
            num_temp = num
            while num_temp:
                s += num_temp % 10
                num_temp //= 10
            digi_count[s].append(num)

        # 在每組數字中找最大兩個並計算和
        max_res = -1
        for int_list in digi_count.values():
            list_len = len(int_list)
            if list_len > 1:
                if list_len == 2:
                    max_res = max(max_res, sum(int_list))
                else:
                    max_two = heapq.nlargest(2, int_list)
                    max_res = max(max_res, sum(max_two))
        return max_res


nums = [18, 43, 36, 13, 7]
# nums = [10, 12, 19, 14]
print(Solution().maximumSum(nums))
