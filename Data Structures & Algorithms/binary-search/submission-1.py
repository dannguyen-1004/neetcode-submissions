class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pointer = len(nums) // 2

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        while(left != pointer and right != pointer):
            if(nums[pointer] == target):
                return pointer
            
            if(nums[pointer] < target):
                left = pointer
                pointer = (pointer + right) // 2
            else:
                right = pointer
                pointer = pointer // 2
        
        return -1