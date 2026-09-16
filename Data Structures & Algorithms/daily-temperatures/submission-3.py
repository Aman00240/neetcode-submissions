class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        res=[0]*len(temp)
        stack=[]

        for i,t in enumerate(temp):
            while stack and t>stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]= i-stackInd

            stack.append([t,i])
        
        return res