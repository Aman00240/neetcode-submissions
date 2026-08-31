class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        seen={}
        for i in arr:
            if i in seen:
                return True
            
            seen[i]=True
        return False


print(Solution().hasDuplicate([1, 2, 3, 3]))
   