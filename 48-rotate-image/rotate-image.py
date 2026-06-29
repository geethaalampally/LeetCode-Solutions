class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        li=[]
        for i in range(n):
            for j in range(n):
                li.append(matrix[i][j])
        idx=0
        for i in range(n-1,-1,-1):
            for j in range(n):
                matrix[j][i]=li[idx]
                idx+=1


    #  approach 2 optimal 
    # for i in range(n):
    #         for j in range(i):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #     # Step 2: Reverse each row
    #     for i in range(n):
    #         left = 0
    #         right = n - 1

    #         while left < right:
    #             matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
    #             left += 1
    #             right -= 1