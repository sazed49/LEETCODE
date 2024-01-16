



class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!=1:
            sum=0
            while n>0:
                digit=n%10
                sum+=digit**2
                n=n//10
            if sum in visited: return False

            visited.add(sum)
            n=sum

        return True

sol = Solution()
a=sol.isHappy(2)
print(a)
