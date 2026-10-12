class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        word = {}
        for char in s:
            if char in word:
                word[char]+=1
            else:
                word[char]=1

        for char in t:
            if char in word and word[char]>=1:
                word[char]-=1
            else:
                return False
        return True
        
