import itertools
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        s=0
        for i in itertools.combinations(nums,2):
            if i[0]^i[1]>s:
                s=i[0]^i[1]
        return s