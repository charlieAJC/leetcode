class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()
        a, b, c = nums

        # 1. 是不是三角形？
        if a + b <= c:
            return "none"

        # 2. 是哪一種三角形？
        if a == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"


nums = [3, 3, 3]
# Output: "equilateral"

nums = [3, 4, 5]
# Output: "scalene"

Solution().triangleType(nums)
