# def fun(v1,v2):
# 	v1=v1.split(".")
# 	v2=v2.split(".")
# 	if len(v1)>len(v2):
# 		for _ in range(len(v1)):
# 			v2.append(0)
# 	if len(v1)<len(v2):
# 		for _ in range(len(v2)):
# 			v1.append(0)
# 	# print(v1,v2)
# 	for x in range(min(len(v1),len(v2))):
# 		if int(v1[x])==int(v2[x]):
# 			continue
# 		if int(v1[x])>int(v2[x]):
# 			return 1
# 		if int(v1[x])< int(v2[x]):
# 			return -1
# 	return 0

# print(fun("0.1","1.1"))
# print(fun("1.0.1","1"))
# print(fun("7.5.2.4","7.5.3"))
# print(fun("1.01","1.001"))
# print(fun("1","1.1"))


# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1=version1.split(".")
#         v2=version2.split(".")
#         if len(v1)>len(v2):
#             for _ in range(len(v1)):
#                 v2.append(0)
#         if len(v1)<len(v2):
#             for _ in range(len(v2)):
#                 v1.append(0)
#         # print(v1,v2)
#         for x in range(min(len(v1),len(v2))):
#             if int(v1[x])==int(v2[x]):
#                 continue
#             if int(v1[x])>int(v2[x]):
#                 return 1
#             if int(v1[x])< int(v2[x]):
#                 return -1
#         return 0

def fun(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==s[1]:
        # x=s[0]
        # i=1
        while len(s)>1 and s[1]==s[0] :
            s=s[1:]
        return  fun(s[1:])
    else:
        return s[0]+fun(s[1:])
for _ in range(int(input())):
    print(fun(input()))