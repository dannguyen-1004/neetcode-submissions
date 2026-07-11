class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        print(numsSet)
        return len(numsSet) != len(nums)