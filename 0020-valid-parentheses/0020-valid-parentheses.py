class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            "(" :")",
            "{":"}",
            "[":"]"
        }
        if len(s)==1:
            return False
        stack=[]
        for i in s:
            if i in dict:
                stack.append(i)
            elif i in dict and not stack:
                return False
            else:
                if stack and dict[stack.pop()]==i:
                    pass
                else:
                    return False
        if stack:
            return False
        return True
