class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        process = [[0] * 26 for _ in range(t + 1)]
        for char in s:
            process[0][ord(char) - ord("a")] += 1
        for i in range(1, t + 1):
            process[i][0] = process[i - 1][25]
            process[i][1] = process[i - 1][0] + process[i - 1][25]
            for j in range(2, 26):
                process[i][j] = process[i - 1][j - 1]
        return sum(process[t]) % (10**9 + 7)


# s = "abcyy"
# t = 2
# Output: 7

s = "azbk"
t = 1
# Output: 5

print(Solution().lengthAfterTransformations(s, t))
