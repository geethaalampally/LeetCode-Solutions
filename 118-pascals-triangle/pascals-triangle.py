
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def ncr(n, r):
            res = 1
            for i in range(r):
                res = res * (n - i)
                res = res / (i + 1)
            return int(res)

        ans = []

        for row in range(1, numRows + 1):
            temp = []

            for col in range(1, row + 1):
                val = ncr(row - 1, col - 1)
                temp.append(val)

            ans.append(temp)

        return ans