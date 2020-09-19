def fun(arr):
	max_sum=0
	if len(arr)==0:
		return max_sum

	s=arr[0]
	
	for i in range(1,len(l)):
		if arr[i]-s>max_sum:
			max_sum = arr[i]-s
		if arr[i]<s:
			s=arr[i]
	return max_sum

l=[7,6,4,3,1]     #output = 0
l=[]			  #output = 0
l=[7,1,5,3,6,4]	  #output = 5
print(fun(l))



#___________________________Leetcode Solution_________________________________-


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        if len(prices) ==0:
            return max_sum
        
        small = prices[0]
        
        for i in range(1,len(prices)):
            dif = prices[i]-small
            if dif > max_sum:
                max_sum = dif
            
            if small > prices[i]:
                small = prices[i]
        return max_sum