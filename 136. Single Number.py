from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}

        # print(hash)
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        #print(hash)
        return  min(hash, key=hash.get)


        #print(hash)
sol = Solution()
nums=[4,1,2,1,2]
ans=sol.singleNumber(nums)
print(ans)