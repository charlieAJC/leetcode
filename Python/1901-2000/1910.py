class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        part_list = list(part)
        part_len = len(part)
        res = []
        for char in s:
            res.append(char)
            if len(res) >= part_len and res[-part_len:] == part_list:
                # 為避免重複建立新物件，改用 del 移除匹配字串
                # res = res[:-part_len]
                del res[-part_len:]
        return "".join(res)


# s = "daabcbaabcbc"
# part = "abc"
# Output: "dab"

s = "axxxxyyyyb"
part = "xy"
# Output: "ab"
print(Solution().removeOccurrences(s, part))
