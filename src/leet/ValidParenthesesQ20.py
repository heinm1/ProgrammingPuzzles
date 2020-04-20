
# Parentheses Matching algorithom
# O(n) Time complexity (n = len(s))
# O(n) Space complexity (n = len(s), max potential size of stack)
class Solution:

    inverse = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif self.inverse.get(c) != None and stack[-1] == self.inverse[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0



s = Solution()
assert s.isValid("()") == True, "Should be true"
assert s.isValid("()[]{}") == True, "Should be true"
assert s.isValid("(]") == False, "Should be false"
assert s.isValid("([)]") == False, "Should be false"
assert s.isValid("{[]}") == True, "Should be true"
assert s.isValid("()") == True, "Should be true"