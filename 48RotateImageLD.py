"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]


n = len(matrix)


for i in reversed(range(n)):
    for j in range(n):
        p = matrix[i][j]
        print(i,j,p)


#Matrix2 = [[0]*n]*n
#Matrix2 = [[]]*n
Matrix2 = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        #Matrix2[i][j] = matrix[j][i]
        Matrix2[i].append(matrix[j][i])

for i in range(n):
    Matrix2[i].reverse()
print(Matrix2)
"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n= len(matrix)

        Matrix2 = [[] for i in range(n)]

        for i in range(n):
            for j in range(n):
                Matrix2[i].append(matrix[j][i])

        for i in range(n):
            Matrix2[i].reverse()

        for i in range(n):
            matrix[i] = Matrix2[i]


