class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]


print(Solution().convertTemperature(36.50))
print(Solution().convertTemperature(122.11))
