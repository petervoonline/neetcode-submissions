class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for i in nums:
            tmp_subset = []
            for j in ret:
                tmp = j.copy()
                tmp.append(i)
                tmp_subset.append(tmp)
            ret.extend(tmp_subset)
            
        return ret

        
        
        

