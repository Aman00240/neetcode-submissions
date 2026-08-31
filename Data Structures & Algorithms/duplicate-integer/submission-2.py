class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    return True
        
        return False


print(Solution().hasDuplicate([1, 2, 3, 3]))
   