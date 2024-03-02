from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        d = ''.join(map(str, digits))
       # print(d)
        an=int(d)
        b=an+1
        digits_list = [int(digit) for digit in str(b)]
        return  (digits_list)





sol = Solution()
digits = [4,3,2,1]
ans=sol.plusOne(digits)
print(ans)