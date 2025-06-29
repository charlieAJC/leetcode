class Solution(object):
    def clearDigits(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        element_list = []
        for element in s:
            if element.isdigit():
                element_list.pop()
            else:
                element_list.append(element)
        return "".join(element_list)


# s = "abc"
# Output: "abc"
s = "cb34"
# Output: ""
print(Solution().clearDigits(s))
