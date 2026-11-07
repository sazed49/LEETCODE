class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        differences = []
        points.sort(key=lambda x: x[0])
        for i in range(1,len(points) ):
            differences.append(points[i][0]-points[i-1][0])
        return max(differences)
        
s=Solution()
print(s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))