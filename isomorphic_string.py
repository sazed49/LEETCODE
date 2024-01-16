

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_mapping = {}
        f=0

        # Iterate through the characters of the strings and create the mapping
        for char1, char2 in zip(s, t):
            if char1 not in char_mapping:
                char_mapping[char1] = [char2]
            else:
                char_mapping[char1].append(char2)
        #for key, values in char_mapping.items():
            #print(f"{key}:{','.join(values)}")
        for key, values in char_mapping.items():
            #print(set(values))

            if len(set(values)) > 1:
                #print("paisi")
                f=1
                break

        #print(f)
        second_mapping = {}
        g = 0

        # Iterate through the characters of the strings and create the mapping
        for char1, char2 in zip(t, s):
            if char1 not in second_mapping:
                second_mapping[char1] = [char2]
            else:
                second_mapping[char1].append(char2)
        #for key, values in second_mapping.items():
           # print(f"{key}:{','.join(values)}")
        for key, values in second_mapping.items():
            #print(set(values))

            if len(set(values)) > 1:
                g= 1
                break

        #print(f)
        if f or g:
            return False
        else:
            return True





sol = Solution()
s="foo"
t="bar"
ans=sol.isIsomorphic(s,t)
print(ans)