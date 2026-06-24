class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []
        
        def dfs(i: int) -> None:
            if i >= len(nums):
                ret.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1) # include
            subset.pop()
            dfs(i + 1) # exclude

        dfs(0)
        return ret
        """
        # ITERATIVE
        ret = [[]]
        for i in nums:
            tmp_subset = []
            for j in ret:
                tmp = j.copy()
                tmp.append(i)
                tmp_subset.append(tmp)
            ret.extend(tmp_subset)
            
        return ret"""

        
        
        

