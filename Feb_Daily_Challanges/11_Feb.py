class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = [0] * 256
        for i in s:
            c[ord(i)] += 1
            
        for j in t:
            c[ord(j)] -= 1
            
        for e in c:
            if e != 0 :
                return False
        return True
        
