class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        triplets = []

        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue

            l = i + 1
            r = len(sortedNums) - 1

            while l < r:
                total = sortedNums[i] + sortedNums[l] + sortedNums[r]

                if total == 0:
                    triplets.append([
                        sortedNums[i],
                        sortedNums[l],
                        sortedNums[r]
                    ])

                    l += 1
                    r -= 1

                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1

                    while l < r and sortedNums[r] == sortedNums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1

                else:
                    r -= 1

        return triplets