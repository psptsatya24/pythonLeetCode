import re
class ReverseWords_151:
    def reverseWords(self, s: str) -> str:
        s =  s.strip()
        wordsList = re.split(r'\s+', s)
        i=0
        j= len(wordsList)-1

        while ( i< j ):
            temp = wordsList[j]
            wordsList[j] = wordsList[i]
            wordsList[i] = temp
            i= i +1
            j= j-1

        s = ' '.join(wordsList)
        return s



obj = ReverseWords_151()
print(obj.reverseWords('example   good a'))