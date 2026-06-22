class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        print(nums)
        med=0
        n=len(nums)
        if n%2==0:
            val=nums[n//2]+nums[(n//2)-1]
            med=val/2
        else:
            val=nums[n//2]
            med=val
        return med