class Candies_1431:
    def kidsWithCandies(self, candies, extraCandies) -> [bool]:
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        #get max from array
        maxValue = max(candies)
        res=[]
        for i in range (0, len(candies)):
            if extraCandies + candies[i] >= maxValue :
                res.insert(i,True)
            else:
                res.insert(i,False)

        return res

obj=Candies_1431();
candies=[4,2,1,1,2]
print(obj.kidsWithCandies(candies, 2))