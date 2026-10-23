class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = int(tokens[0])

        for t in tokens:
            if t == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif t == "-":
                res = -(stack.pop() - stack.pop())
                stack.append(res)
            elif t == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif t == "/":
                first = stack.pop()
                res = int(stack.pop() / first)
                stack.append(res)
            else:
                stack.append(int(t))
            
        return res