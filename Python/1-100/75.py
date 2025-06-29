class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法一
        # p0 統計 0 的個數，p1 統計 0 和 1 的個數
        p0 = p1 = 0
        for ind, num in enumerate(nums):
            nums[ind] = 2
            if num <= 1:
                nums[p1] = 1
                p1 += 1
            if num == 0:
                nums[p0] = 0
                p0 += 1
        print(nums)
        # ====================================
        # 方法二
        # 定義三個指針 i, j, k
        # 指針 i 用於指向陣列中值為 0 的右邊界
        # 指針 j 用於指向陣列中值為 2 的左邊界
        # 指針 k 用於指向當前遍歷的元素
        # i = -1
        # j = len(nums)
        # k = 0
        # while k < j:
        #     if nums[k] == 0:
        #         i += 1
        #         nums[i], nums[k] = nums[k], nums[i]
        #         k += 1
        #     elif nums[k] == 2:
        #         j -= 1
        #         nums[j], nums[k] = nums[k], nums[j]
        #     else:
        #         k += 1
        # print(nums)


# nums = [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]

nums = [2, 0, 1]
# Output: [0, 1, 2]

Solution().sortColors(nums)
