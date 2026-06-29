class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        co=Counter(nums)
        res=0
        for num in co:
            if co[num]%k==0:
                res+=num*co[num]
        return res
        