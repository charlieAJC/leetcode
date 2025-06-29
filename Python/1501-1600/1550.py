class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        pointer = 0
        arr_len = len(arr)
        while pointer + 3 <= arr_len:
            even_pointer = None
            for i in range(pointer, pointer + 3):
                if arr[i] % 2 == 0:
                    even_pointer = i
            if even_pointer == None:
                return True
            pointer = even_pointer + 1
        return False


# arr = [2,6,4,1]
# Output: false

# arr = [1,2,34,3,4,5,7,23,12]
# Output: true

arr = [1, 2]
# Output: false

print(Solution().threeConsecutiveOdds(arr))
