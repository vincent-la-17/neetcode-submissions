class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                if i == "+":
                    inter = o1+o2
                    stack.append(inter)
                elif i == "-":
                    inter = o2-o1
                    stack.append(inter)
                elif i == "*":
                    inter = o2*o1
                    stack.append(inter)
                else:
                    inter = int(o2/o1)
                    stack.append(inter)
            
        return int(stack[-1])