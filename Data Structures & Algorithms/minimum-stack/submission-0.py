class MinStack:

    def __init__(self):
        self.minStack = []
        self.prefixMinStack = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        tmp = val
        if len(self.prefixMinStack) >= 1:
            tmp = min(self.prefixMinStack[-1], val)
        self.prefixMinStack.append(tmp)
        

    def pop(self) -> None:
        self.prefixMinStack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        print(self.prefixMinStack)
        return self.prefixMinStack[-1]


        
