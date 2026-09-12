class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'()', '[]', '{}'}
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack and stack[-1] + c in valid_pairs:
                    stack.pop()

                else:
                    return False
        
        return not stack