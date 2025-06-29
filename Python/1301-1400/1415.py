class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # version 1
        # result = []
        # happy_alphabet = ["a", "b", "c"]
        # temp_list = []

        # def backtrack(start: int):
        #     if start == n:
        #         result.append("".join(temp_list))
        #         return

        #     for alpha in happy_alphabet:
        #         if start == 0:
        #             temp_list.append(alpha)
        #             backtrack(start + 1)
        #             temp_list.pop()
        #         else:
        #             if alpha != temp_list[-1]:
        #                 temp_list.append(alpha)
        #                 backtrack(start + 1)
        #                 temp_list.pop()

        # backtrack(0)
        # return result[k - 1] if len(result) >= k else ""

        # ======================================================================
        # version 2(improved by ChatGPT)
        total_count = 3 * (2 ** (n - 1))  # 總共有幾個快樂字串
        if k > total_count:
            return ""  # 超出範圍，回傳空字串

        happy_alphabet = ["a", "b", "c"]
        result = []
        k -= 1  # 轉成 0-based index

        for i in range(n):
            group_size = 2 ** (n - i - 1)  # 每個字元選擇的字串數量
            index = k // group_size  # 決定當前應該選哪個字母
            k %= group_size  # 更新 k，確保接下來選擇正確的字元
            print(f"group_size: {group_size}, index: {index}, k: {k}")

            # 確保不與前一個字母相同
            for ch in happy_alphabet:
                print(f"ch: {ch}")
                if not result or result[-1] != ch:
                    if index == 0:
                        result.append(ch)
                        break
                    index -= 1

        return "".join(result)


# n = 1
# k = 3

# n = 1
# k = 4

n = 3
k = 9

# n = 2
# k = 7

# n = 10
# k = 100

print(Solution().getHappyString(n, k))
