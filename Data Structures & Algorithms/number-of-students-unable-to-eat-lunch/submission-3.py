class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = 0
        c = 0
        for i in students:
            if i == 0:
                c += 1
            else:
                s += 1
        for i in sandwiches:
            if i == 0: 
                if c > 0:
                    c -= 1
                else:
                    return c + s
            elif i == 1:
                if s > 0:
                    s -= 1
                else:
                    return c + s
        return 0
                

