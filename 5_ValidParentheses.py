# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={")":"(","]":"[","}":"{"}
        
        for c in s:
            if c in hm:
                if len(stack)>0 and hm[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack)==0