class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for i in range(len(operations)):
            tmp = 0
            if operations[i] == "+":
                tmp =  stack[-1] +  stack[-2]
            elif operations[i] == "D":
                tmp =  stack[-1]*2
            elif operations[i] == "C":
                res -= stack[-1]
                stack.pop()
                continue
            else:
                tmp =  int(operations[i])
            res += tmp
            stack.append(tmp)
        return res


        