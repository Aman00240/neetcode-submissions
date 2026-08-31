class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe={}

        for i in nums:
            if i in dupe:
                return True
            dupe[i]=True
        
        return False