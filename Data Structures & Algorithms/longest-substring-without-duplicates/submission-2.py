class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        i = 0
        maxLength = 0

        for j in range(len(s)):
            while s[j] in subSet:
                subSet.remove(s[i])
                i += 1

            subSet.add(s[j])
            maxLength = max(maxLength, j - i + 1)

        return maxLength