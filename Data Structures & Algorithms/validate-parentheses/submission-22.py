class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_pair = {'}': '{', ']':'[', ')':'('}
        for p in s:
            if p in p_pair:
                if stack and stack[-1] == p_pair[p]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(p)
        return True if not stack else False 

            