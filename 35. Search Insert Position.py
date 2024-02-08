from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l <= r:

            mid = l + (r - l) // 2

            # Check if x is present at mid
            if nums[mid] == target:
                return mid

            # If x is greater, ignore left half
            elif nums[mid] < target:
                l = mid + 1

            # If x is smaller, ignore right half
            else:
                r = mid - 1
        nums.append(target)
        s=sorted(nums)
        #print(s)
        return s.index(target)
sol = Solution()
nums=[1,3,5,6]
target=7
ans=sol.searchInsert(nums,target)
print(ans)