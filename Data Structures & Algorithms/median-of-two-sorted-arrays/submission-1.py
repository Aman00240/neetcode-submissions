class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=sorted(nums1+nums2)
        l,r=0,len(merged)-1
        m=(l+r)//2

        if len(merged)%2==0:
            return (merged[m]+merged[m+1])/2
        
        else:
            return merged[m]