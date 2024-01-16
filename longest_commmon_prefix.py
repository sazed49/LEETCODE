from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=[]
        for chars_at_index in zip(*strs):

            if all(char == chars_at_index[0] for char in chars_at_index):

                print(f"Characters at index {chars_at_index}: match.")
                a.append(chars_at_index[0])

            else:
                break
        s = ''.join(a)

        if not s:
            s=""
            return  s
        else:
            return s

# Iterate through corresponding characters at the same index


solu = Solution()
ans=solu.longestCommonPrefix(["flower","flow","flight"])
print(ans)
