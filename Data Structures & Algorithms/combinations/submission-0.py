class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        subset = []

        def dfs(i: int) -> None:
            if len(subset) == k:
                ret.append(subset.copy())
                return  
            elif i > n or len(subset) > k:
                return
            subset.append(i)
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(1)
        return ret