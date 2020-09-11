import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max=sys.maxsize
        res=-Max
        if 0 in nums:
            res=0
        neg_min=1       # negative minimum
        n=len(nums)
        pro=1
        for i in range(n):
            pro*=nums[i]
            if pro==0: # reset everything
                neg_min=1
                pro=1
                continue
            res=max(res,pro)
            
            if pro<0:
                res=max(res,pro//neg_min)
                if neg_min==1:
                    neg_min=pro
                else:
                    neg_min=max(neg_min,pro)
        return res