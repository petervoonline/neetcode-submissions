class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo = 1
        hi = max(piles)
        ret = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            time = self.totalTime(piles, mid)
            if time > h:
                lo = mid + 1
            elif time <= h:
                ret = mid
                hi = mid - 1

        return ret


    def totalTime(self, piles: List[int], h: int) -> int:
        ret = 0
        for i in piles:
            tmp = (i + h - 1) // h
            ret += tmp
        return ret
        
