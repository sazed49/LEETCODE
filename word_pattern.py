from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        char_mapping={}

        a=list(pattern)
        b=s.split()
        #print(a)
        #print(b)
        if(len(a)!=len(b)):return False
        f=0

        for char1, char2 in zip(a, b):
            if char1 not in char_mapping:
                char_mapping[char1] = [char2]
            else:
                char_mapping[char1].append(char2)
        #for key, values in char_mapping.items():
            #print(f"{key}:{','.join(values)}")
        for key, values in char_mapping.items():
            #print(set(values))
            #print(values[0])


            if (len(set(values))>1 ):
                 f=1
                 break
        g = 0
        new_map={}

        for char1, char2 in zip(b, a):
            if char1 not in new_map:
                new_map[char1] = [char2]
            else:
                new_map[char1].append(char2)
        #for key, values in new_map.items():
            #print(f"{key}:{','.join(values)}")
        for key, values in new_map.items():
            #print(set(values))
            #print(values[0])

            if (len(set(values)) > 1):
                g = 1
                break

        if f or g:
            return  False
        else:
            return  True
sol=Solution()
pattern="aaa"
t="aa aa aa aa"
ans=sol.wordPattern(pattern,t)
print(ans)