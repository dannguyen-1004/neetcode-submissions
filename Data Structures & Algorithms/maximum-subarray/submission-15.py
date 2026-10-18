class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rid = nums[0]
        maxresult = rid

        l = 0
        r = 0

        while r < len(nums) - 1:

            if rid < 0:
                r += 1
                l = r
                rid = nums[l]
            else:
                r += 1
                rid += nums[r]

            maxresult = max(rid, maxresult)

        return maxresult