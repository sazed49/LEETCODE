from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
sol = Solution()
mylist = [3,2,3]
k=sol.majorityElement(mylist)
print(k)
