def fun(s1,s2):
	S1=[]
	S2=[]
	for x in s1:
		S1.append(x)
	for i in s2:
		S2.append(i)
	b=0
	for x in range(len(s1)):
		if S1[x] == S2[x]:
			b+=1
			S1[x]=-9
			S2[x]=-12

	c=0
	for i in range(len(S1)):
		if S1[i] in S2:
			S2.remove(S1[i])
			c+=1

	return str(b)+"A"+str(c)+"B"
	
print(fun("1123","0111"))



# _________________________OR___________________LeetCode Solution

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        S1=[]
        S2=[]
        for x in secret:
            S1.append(x)
        for i in guess:
            S2.append(i)
        b=0
        for x in range(len(secret)):
            if S1[x] == S2[x]:
                b+=1
                S1[x]=-9
                S2[x]=-12

        c=0
        for i in range(len(S1)):
            if S1[i] in S2:
                S2.remove(S1[i])
                c+=1
        return str(b)+"A"+str(c)+"B"