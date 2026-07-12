class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
    
        #left product
        left = [1] * len(nums)
        for i in range(len(nums)):
            if(i > 0):
                left[i] = nums[i - 1] * left[i - 1]
            else:
                left[i] = 1

            answer[i] = left[i]

        #right product
        right = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if(i < len(nums) - 1):
                right[i] = nums[i + 1] * right[i + 1]
            else:
                right[i] = 1

            answer[i] *= right[i]

        return answer