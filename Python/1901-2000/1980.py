class Solution(object):
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        :type nums: List[str]
        :rtype: str
        """
        # version 1
        # i = 0
        # res = ""
        # nums_len = len(nums)
        # num_len = len(nums[0])
        # nums.sort()
        # print(nums)
        # while True:
        #     if nums_len > i:
        #         if int(nums[i], 2) != i:
        #             res = str(bin(i))[2:].zfill(num_len)
        #             break
        #     else:
        #         res = str(bin(i))[2:].zfill(num_len)
        #         break
        #     i += 1
        # return res

        # =====================================================================
        # version 2 (improved by ChatGPT)
        num_len = len(nums[0])
        # 由於 set 會建立 hash table，所以做搜尋/插入/刪除的時間複雜度是 O(1)
        # 因此這邊不用 version 1 的做法 nums.sort()，其時間複雜度是 O(n * log n)
        num_set = set(int(num, 2) for num in nums)  # 建立哈希集合

        for i in range(len(nums) + 1):  # 嘗試 0~n 的二進制數
            if i not in num_set:
                return bin(i)[2:].zfill(num_len)  # 回傳二進制格式

        return ""  # 理論上不會到這行


# nums = ["01", "10"]
# Output: "11"

# nums = ["00", "01"]
# Output: "11"

# nums = ["111", "011", "001"]
# Output: "101"

nums = [
    "0000000111",
    "0000001001",
    "0000000100",
    "0000000001",
    "0000000010",
    "1111111111",
    "0000000101",
    "0000000000",
    "0000001000",
    "0000000110",
]
# Output: "0000000011"

print(Solution().findDifferentBinaryString(nums))
