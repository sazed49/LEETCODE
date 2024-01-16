from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            print({"i"},i)

            print({"num"},nums[i])
            print({"i+k"},i+k)
            print({"len"},len(nums))
            if (i+k)>len(nums):
                return False
            elif nums[i+k]==nums[i]:
                return True
            else: continue
        return False





sol=Solution()
nums=[1,2,3,1,2,3]
k=2
ans=sol.containsNearbyDuplicate(nums,k)
print(ans)
