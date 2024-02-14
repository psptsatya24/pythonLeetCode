class GCDofStrings:
    def getGCDString(self, str1 : str, str2 : str) ->  str :
      #str3 = min(len(str1), len(str2))
      s  = ''
      if( len(str2) > len(str1)):
         return  self.getGCDString(str2, str1)

      if (str1 == str2):
          return str1

      if(str1.startswith(str2)):
         return  self.getGCDString(str1[len(str2):],str2)

      return 'none'

obj = GCDofStrings()
print(obj.getGCDString('ABCDABC','ABC'))
