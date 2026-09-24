class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
             if i not in "+-*/":
                stack.append(int(i))
             else:
                o1 = stack.pop()
                o2 = stack.pop()
                if i == "+":
                    stack.append(o1+o2)
                elif i == "-":
                    stack.append(o2-o1)
                elif i == "*":
                    stack.append(o1*o2)
                else:
                    stack.append(int(o2/o1))
        return stack[-1]