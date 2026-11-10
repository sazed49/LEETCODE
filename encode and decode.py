
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for s in strs:
            ans+=str(len(s))+"#"+s
        return ans
          
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<(len(s)):
            j=i
            while j<len(s)and s[j]!="#":
                j+=1
            length=int(s[i:j]) 
            ans.append(s[j+1:j+1+length])
            i=j+1+length
        return ans

solution =  Solution()
strs=["hello","world"]
encoded_string = solution.encode(strs)
print(encoded_string)
decoded_str=solution.decode(encoded_string)
print(decoded_str)

