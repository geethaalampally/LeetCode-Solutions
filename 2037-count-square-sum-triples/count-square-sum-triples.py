class Solution:
    def countTriples(self, n: int) -> int:

        res=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j==i:
                    continue
                val=i*i+j*j
                if math.sqrt(val) in range(1,n+1):
                    res+=1
        return res


        