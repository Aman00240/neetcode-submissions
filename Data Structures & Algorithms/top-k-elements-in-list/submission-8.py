class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #fk bucket sort

        freq={}
        res=[[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num]=freq.get(num,0)+1
        

        for num,index in freq.items():
            res[index].append(num)
        
        out=[]

        for i in range(len(res)-1,-1,-1):
            for num in res[i]:
                out.append(num)
                k-=1
                if k==0:
                    return out