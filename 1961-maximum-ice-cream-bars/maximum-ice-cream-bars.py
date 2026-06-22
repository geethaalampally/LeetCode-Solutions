class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq=[0]*(max(costs)+1)
        for cost in costs:
            freq[cost]+=1
        
        count=0
        for cost in range(len(freq)):
            while freq[cost]>0 and coins>=cost:
                coins-=cost
                count+=1
                freq[cost]-=1
        return count
        