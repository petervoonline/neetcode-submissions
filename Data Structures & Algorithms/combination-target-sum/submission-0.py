class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        subset = []

        def dfs(i: int, sum: int) -> None:            
            if sum == target:
                ret.append(subset.copy())
                return
            elif sum > target or i >= len(nums):
                return
            curVal = nums[i]
            subset.append(curVal)      
            if (sum + curVal) <= target:
                dfs(i, sum + curVal)
            subset.pop()
            dfs(i + 1, sum)

        dfs(0,0)
        return ret