class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}

        for i, value in enumerate(nums):
            remainder = target - value
            
            if remainder in hashNums:
                return [hashNums[remainder], i]

            hashNums[value] = i
