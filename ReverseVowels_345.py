class ReverseVowels_345:
    def reverseVowels(self, s: str) -> str:
       s_array = list(s)
       leftPointer = 0
       rightPointer = len(s)-1

       print(s_array)
       found_match = False

       vowels = ['a', 'e' , 'i' ,'o', 'u', 'A', 'E', 'I', 'O', 'U']

       while(leftPointer < rightPointer and leftPointer < len(s)):
            while(leftPointer < rightPointer and not (s_array[leftPointer]  in vowels)):
                leftPointer+=1
            while(leftPointer < rightPointer and not (s_array[rightPointer] in vowels )):
                rightPointer -= 1
            #Swap
            if leftPointer < rightPointer:
                temp = s_array[rightPointer]
                s_array[rightPointer] = s_array[leftPointer]
                s_array[leftPointer] = temp

            leftPointer+=1
            rightPointer-=1


       s = ''.join(s_array)
       return  s


obj = ReverseVowels_345()
print(obj.reverseVowels('.,'))