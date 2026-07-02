class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen=set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         seen.remove(num)
        # res=list(seen)
        # return res[0]
        
        xor=0
        for num in nums:
            xor=xor^num
        return xor