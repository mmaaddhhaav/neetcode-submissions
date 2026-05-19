class MyQueue:

    def __init__(self):
        self.str1 = []
        self.str2 = []

    def push(self, x: int) -> None:
        while self.str1:
            self.str2.append(self.str1.pop())
        self.str1.append(x)
        while self.str2:
            self.str1.append(self.str2.pop())

    def pop(self) -> int:
        if not self.str1:
            print("Stack is empty")
            return -1
        top_element = self.str1.pop()
        return top_element

    def peek(self) -> int:
        if not self.str1:
            print("Stack is empty")
            return -1
        return self.str1[-1]

    def empty(self) -> bool:
        return not self.str1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()