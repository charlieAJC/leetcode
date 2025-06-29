from collections import defaultdict


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # version 1
        # product_show_time = defaultdict(int)

        # for i in nums:
        #     for j in nums:
        #         if i != j and i < j:
        #             if i * j in product_show_time:
        #                 product_show_time[i * j] += 1
        #             else:
        #                 product_show_time[i * j] = 1

        # res = 0
        # for v in product_show_time.values():
        #     if v > 1:
        #         res += int(((v * (v - 1)) / 2) * 8)
        # return res

        # version 2 (improved by ChatGPT)
        product_show_time = defaultdict(int)

        # 遍歷所有不重複數對
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_show_time[product] += 1

        res = 0
        for v in product_show_time.values():
            # 計算所有四元組數量
            res += (v * (v - 1) // 2) * 8

        return res


# nums = [2, 3, 4, 6]
# nums = [1, 2, 4, 5, 10]
nums = [2, 3, 4, 6, 8, 12]
print(Solution().tupleSameProduct(nums))
