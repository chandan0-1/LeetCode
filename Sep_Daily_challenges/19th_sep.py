class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        valid_nums = []
        for i in range(1,10):
            curr_num = i
            for j in range(i+1,10):
                curr_num = curr_num*10 + j
                if curr_num >= low and curr_num <= high:
                    valid_nums.append(curr_num)
        return sorted(valid_nums)