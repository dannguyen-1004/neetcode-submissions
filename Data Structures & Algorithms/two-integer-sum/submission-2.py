class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}

        for i in range(len(nums)):
            position[nums[i]] = i
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in position and position[remainder] != i:
                return[i, position[remainder]]
        
        return False