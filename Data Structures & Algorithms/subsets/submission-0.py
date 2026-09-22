class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            backtrack(i + 1)

            sol.append(nums[i])  # Choose nums[i]
            backtrack(i + 1)     # Explore all possibilities with this choice
            sol.pop()            # Undo the choice and restore the previous state
        
        backtrack(0)
        return res