class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while r > l:
            i = (r + l) // 2

            if nums[i] > nums[r]:
                l = i + 1
            else:
                r = i

        return nums[l]