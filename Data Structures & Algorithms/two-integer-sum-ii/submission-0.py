class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while True:
            total = numbers[i] + numbers[j]
            if(total == target):
                return [i+1, j+1]
            
            if(total > target):
                j -= 1
            else:
                i += 1
