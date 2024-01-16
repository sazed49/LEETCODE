from typing import List
from collections import Counter

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        new_map=defaultdict(list)
        new2_map=defaultdict(list)
        ans=[]
        f=0
        g=0
        sorted_m = tuple(sorted(magazine))
        #print(sorted_m)
        sorted_r = tuple(sorted(ransomNote))
        #print(sorted_r)

        for  char in magazine:

            new_map[char].append(char)

            #print(new_map)
        for char in ransomNote:
            new2_map[char].append(char)
            #print(new2_map)
        #print(new_map)
        #print(new2_map)
        #all_keys = set(new_map.keys()).union(set(new2_map.keys()))
        #print(new2_map.keys())
        for key in new2_map.keys():
            #print("2 len")
            #print(len(new2_map[key]))
            #print("1 len")
            #print(len(new_map[key]))
            if len(new2_map[key])<=len(new_map[key]):
                f=1
                #print("less tha or eq")

            else:
                g=1
                #print("greater")
        if g:
            return False
        else:
            return True









sol=Solution()
magazine="b"
ramsomNote="a"
ans=sol.canConstruct(ramsomNote,magazine)
print(ans)