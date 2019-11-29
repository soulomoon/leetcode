class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        close_count_down = s.count(')')
        s = list()
        open_count_up = 0
        for i, c in enumerate(s):
            if c == '(':
                if open_count_up == close_count_down:
                    s[i] = '#'
                    continue
                open_count_up += 1
            elif c == ')':
                close_count_down -= 1
                if open_count_up == 0:
                    s[i] = '#'
                    continue
                open_count_up -= 1
        return "".join(s).replace('#', '')

    def minRemoveToMakeValid_slow(self, s: str) -> str:
        stack = []
        rev_stack = []
        # res =
        for i, c in enumerate(s):
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    rev_stack.append(i)
            elif c == "(":
                stack.append(i)
        jump = set()
        jump = jump.union(stack)
        jump = jump.union(rev_stack)
        rev = ""
        for i, c in enumerate(s):
            if i not in jump:
                rev += c
        return rev
