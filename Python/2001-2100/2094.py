from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            parts = [num // 100, (num // 10) % 10, num % 10]
            count = Counter(parts)
            if all(freq[d] >= count[d] for d in count):
                res.append(num)
        return res


# digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]

digits = [2, 2, 8, 8, 2]
# Output: [222,228,282,288,822,828,882]

# digits = [3,7,5]
# Output: []

print(Solution().findEvenNumbers(digits))
