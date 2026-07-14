class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map={'()','{}','[]'}
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif not stack or stack.pop() + i not in brackets_map:
                return False
        return not stack
