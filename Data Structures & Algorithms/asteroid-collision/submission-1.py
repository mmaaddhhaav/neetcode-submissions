class Solution(object):
    def asteroidCollision(self, ast):
        n = len(ast)
        stack = []
        for i in range(0,n):
            if ast[i] > 0:
                stack.append(ast[i])
            else:
                while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(ast[i]):
                    stack.pop()
                if len(stack) != 0 and stack[-1] == abs(ast[i]):
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(ast[i])
        return stack