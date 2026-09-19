class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
                print(stack)
            else:
                if len(stack) == 0:
                    return False
                if s[i] == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif s[i] == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif s[i] == ']':
                   
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0