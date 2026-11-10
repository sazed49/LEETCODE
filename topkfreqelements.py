from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts=Counter(nums)
        ans=[]
        for _ in range(k):
            highest=0
            for num,count in counts.items():
                if count>highest:
                    highest=count
                    most_freq=num
            ans.append(most_freq)
            counts.pop(most_freq)
        return ans


s=Solution()
print(s.topKFrequent([7,7],1))
