class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            left = num - 1
            if left not in numsSet:
                right = num + 1
                k = 1
                while right in numsSet:
                    k += 1
                    right += 1
                
                longest = max(longest, k)

        return longest
        