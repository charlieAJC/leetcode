class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff_index = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_index.append(i)
                if len(diff_index) > 2:
                    return False

        if len(diff_index) == 0:
            return True
        elif len(diff_index) != 2:
            return False
        else:
            if (
                s1[diff_index[0]] == s2[diff_index[1]]
                and s1[diff_index[1]] == s2[diff_index[0]]
            ):
                return True
            return False


# s1 = "bank"
# s2 = "kanb"

# s1 = "attack"
# s2 = "defend"

s1 = "kelb"
s2 = "kelb"

print(Solution().areAlmostEqual(s1, s2))
