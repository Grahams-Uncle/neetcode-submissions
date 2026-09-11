class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for c in tokens:
            if c in '+-*/':
                b = stack.pop()
                a = stack.pop()
                res = 0
                if c == '+':
                    res = a + b
                elif c == '-':
                    res = a - b
                elif c == '*':
                    res = a * b
                else:
                    res = a / b
                stack.append(int(res))
            else:
                stack.append(int(c))
        return stack[0]