



class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!=1:
            sum=0

            if sum in visited: return False

            visited.add(sum)
            n=sum

        return True

sol = Solution()
a=sol.isHappy(2)
print(a)
