class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # arr=[]
        # for i in range(len(nums)):
        #     arr.append((nums[i],i))
        # arr.sort()
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     sumi=arr[i][0]+arr[j][0]
        #     if sumi==target:
        #         return [arr[i][1],arr[j][1]]
        #     if sumi<target:
        #         i+=1
        #     else:
        #         j-=1
        hash={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in hash:
                return [hash[req],i]
            else:
                hash[nums[i]]=i
        return 
            