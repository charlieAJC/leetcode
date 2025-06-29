class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        ans = [words[0]]
        tmp = groups[0]
        for ind, group in enumerate(groups):
            if tmp != group:
                ans.append(words[ind])
                tmp = group
        return ans


# words = ["e", "a", "b"]
# groups = [0, 0, 1]
# Output: ["e","b"]

words = ["a", "b", "c", "d"]
groups = [1, 0, 1, 1]
# Output: ["a","b","c"]

print(Solution().getLongestSubsequence(words, groups))
