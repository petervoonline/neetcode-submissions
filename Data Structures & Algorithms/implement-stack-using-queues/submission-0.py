class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_val = 0

    def push(self, x: int) -> None:
        self.top_val = x
        self.q.append(x)
        for i in range(len(self.q) - 1):
            tmp = self.q.popleft()
            self.q.append(tmp)
        

    def pop(self) -> int:
        res = self.q.popleft()
        if self.q:
            self.top_val = self.q[0]
        return res

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()