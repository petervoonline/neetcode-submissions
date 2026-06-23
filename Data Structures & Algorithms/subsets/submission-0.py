class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for i in nums:
            tmp = ret.copy()
            for j in tmp:
                tmp = j.copy()
                tmp.append(i)
                ret.append(tmp)
            
        return ret

        
        
        

