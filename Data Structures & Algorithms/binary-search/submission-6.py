class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums) // 2
        l = 0
        r = len(nums) - 1
        if nums[i] == target:
            return i
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        while r > l and i!=r and i!=l:
            if nums[i] == target:
                return i
            if nums[i] < target:
                l = i
                i += (r - l) // 2
            elif nums[i] > target:
                r = i
                i //=2
            print("l " + str(nums[l]))
            print("r " + str(nums[r]))
        
        return -1
            