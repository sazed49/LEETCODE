from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        #print(hash)
        for i in range(len(nums)):
            if nums[i] in hash and abs(i-hash[nums[i]]<=k):
                return True
            hash[nums[i]] = i
            #print(hash)
        return False




sol=Solution()
nums=[1,2,3,1,2,3]
k=2
ans=sol.containsNearbyDuplicate(nums,k)
print(ans)
