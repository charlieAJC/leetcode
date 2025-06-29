class Solution:
    def minSum(self, nums1, nums2):
        nums1_sum = 0
        nums2_sum = 0
        nums1_zero_count = 0
        nums2_zero_count = 0

        for n1 in nums1:
            if n1 == 0:
                nums1_zero_count += 1
            else:
                nums1_sum += n1
        for n2 in nums2:
            if n2 == 0:
                nums2_zero_count += 1
            else:
                nums2_sum += n2

        if (nums1_zero_count == 0 and nums1_sum < nums2_sum + nums2_zero_count) or (
            nums2_zero_count == 0 and nums2_sum < nums1_sum + nums1_zero_count
        ):
            return -1
        return max(nums1_sum + nums1_zero_count, nums2_sum + nums2_zero_count)


# nums1 = [3,2,0,1,0]
# nums2 = [6,5,0]
# Output: 12

# nums1 = [2,0,2,0]
# nums2 = [1,4]
# Output: -1

# nums1 = [8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0]
# nums2 = [29,1,6,0,10,24,27,17,14,13,2,19,2,11]
# Output: 179

nums1 = [9, 5]
nums2 = [15, 12, 5, 21, 4, 26, 27, 9, 6, 29, 0, 18, 16, 0, 0, 0, 20]
# Output: -1

print(Solution().minSum(nums1, nums2))
