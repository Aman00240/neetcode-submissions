class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={')':'(','}':'{',']':'['}


        for brkt in s:
            if brkt in closeToOpen:
                if stack and stack[-1]==closeToOpen[brkt]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(brkt)
        
        return True if not stack else False