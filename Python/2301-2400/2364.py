from collections import defaultdict


class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 統計 nums[i] - i 的頻率
        counter_dict = defaultdict(lambda: 0)
        for i in range(len(nums)):
            counter_dict[nums[i] - i] += 1

        # 計算總配對數量
        nums_len = len(nums)
        total_pairs = (nums_len * (nums_len - 1)) // 2

        # 扣除所有符合條件的 Good Pairs 數量
        for count in counter_dict.values():
            if count > 1:
                total_pairs -= (count * (count - 1)) // 2

        return total_pairs


# nums = [4, 1, 3, 3]
nums = [1, 2, 3, 4, 5]
print(Solution().countBadPairs(nums))

# ===========
# 總共會有 Cn 取 2 次比對
# nums = [4, 1, 3, 3],    n = 4, 有  6 次比對, ans = 5
# nums = [1, 2, 3, 4, 5], n = 5, 有 10 次比對, ans = 0
