class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len (s) != len(t):
            return False
        num =[0] * 26
        for i in range(len(s)):
            num[ord(s[i])-ord('a')] += 1
            num[ord(t[i])-ord('a')] -= 1
        for val in num:
            if val !=0:
                return False
        return True 