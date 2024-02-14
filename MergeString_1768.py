#string1 ='abc'
#string2 = 'pqr'
class Solution:
    def mergeStrings(self, s1: str, s2: str) -> str :
         i,j =0,0
         res = []
         while i< len(s1) and j < len(s2) :
             res.append(s1[i])
             res.append(s2[j])
             i+=1
             j+=1
         res.append(s1[i:])
         res.append(s2[j:])
         return ''.join(res)

obj  = Solution()
print(obj.mergeStrings('ab', 'pqr'))