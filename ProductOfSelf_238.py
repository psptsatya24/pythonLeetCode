from functools import reduce
from typing import List

class ProductOfSelf_238:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =1
        postfix=1
        res = [1]  * len(nums)
        for j in range (len(nums)) :
                res[j] = prefix
                prefix = prefix * nums[j]
        for i in range (len(nums)-1, -1, -1) :
                res[i] = res[i] *  postfix
                postfix = postfix * nums[i]  
        return res


obj = ProductOfSelf_238()
num=[1,2,3,4]
print(obj.productExceptSelf(num))