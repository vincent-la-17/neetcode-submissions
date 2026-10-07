class Solution:
    def checkValidString(self, s: str) -> bool:
        # Store the indices of unmatched '(' characters
        stack = []

        # Store the indices of '*' characters
        # A '*' can potentially act as '(' or ')'
        starStack = []

        # Go through each character and its index
        for i, ch in enumerate(s):

            if ch == "(":
                # Store the index of an opening parenthesis
                stack.append(i)

            elif ch == "*":
                # Store the index of a '*'
                starStack.append(i)

            else:  # ch == ")"

                # If there is no '(' or '*' available to match
                # this ')', the string cannot be valid
                if not stack and not starStack:
                    return False

                # Prefer using an actual '(' to match ')'
                if stack:
                    stack.pop()

                # Otherwise, use '*' as an opening parenthesis
                else:
                    starStack.pop()

        # At this point, there may still be unmatched '('.
        # Try to use '*' after the '(' to act as ')'.
        while stack and starStack:

            # The '(' must appear BEFORE the '*' for the '*'
            # to act as its closing ')'.
            if stack.pop() > starStack.pop():
                return False

        # If any '(' are still unmatched, the string is invalid.
        return not stack