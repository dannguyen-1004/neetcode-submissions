class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}
    
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in position and position[remainder] != i:
                return[position[remainder], i]
            else: 
                position[nums[i]] = i
        
        return False