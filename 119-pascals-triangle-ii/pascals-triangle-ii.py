class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex+1
        res=[1]
        val=1
        for c in range(1,n):
            val=val*(n-c)
            val=val//c
            res.append(val)
        return res



        