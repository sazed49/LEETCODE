class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)


        if index != -1:
            r=index
            #print(f"The substring '{sub_string}' is found at index {index}.)
        else:
            r=-1
        return r



sol = Solution()
haystack = "sadbutsad"
needle = "sad"
ans=sol.strStr(haystack,needle)
print(ans)

