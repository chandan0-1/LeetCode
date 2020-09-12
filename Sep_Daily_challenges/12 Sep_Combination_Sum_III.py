import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        temp = [list(l) for l in itertools.combinations(range(1,10),k) if sum(l) == n ]
        return temp