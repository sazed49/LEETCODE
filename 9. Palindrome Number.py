class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        #print(x)
        l=[]
        for i in range(len(s)-1,-1,-1):
            l.append(s[i])
        #print(l)
        ans=''.join(l)
        #print(ans)
        if ans==s:
            return True
        else:
            return False




s=Solution()
x=1221
print(s.isPalindrome(x))