class Solution:
   
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = two
            two = two + temp  

        return two


# 1 1 1-(1 +1) 2-(1+1 +1) (1+1+1 +1+1)