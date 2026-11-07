from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
s=Solution()
if(s.hasDuplicate([1,2,3,4,5,1])):
    print("true")
else:
    print("false")