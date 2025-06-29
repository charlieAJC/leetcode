class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


print(Solution().smallestEvenMultiple(5))
print(Solution().smallestEvenMultiple(6))
