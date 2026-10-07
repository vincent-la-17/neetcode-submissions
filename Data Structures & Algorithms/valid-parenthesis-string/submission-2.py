class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == "*":
                starStack.append(i)
            else:
                if not stack and not starStack:
                    return False
                if stack:
                    stack.pop()
                else:
                    starStack.pop()
        while stack and starStack:
            if stack.pop() > starStack.pop():
                return False
        return not stack