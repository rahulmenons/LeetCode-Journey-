
class Solution(object):
    def generate(self, numRows):

        triangles = []

        for i in range(numRows) :
            rows = [1] * (i+1)
            
            for j in range (1,i):
                rows[j] = triangles[i-1][j-1] + triangles[i-1][j]
            
            triangles.append(rows)

        return triangles
