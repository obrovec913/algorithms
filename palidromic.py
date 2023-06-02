class Solution:
    def longestPalindrome(self, s: str) -> str:
        an = ""
        if  len(s) == 1:
            return s

        for i in range(1, len(s)-1):
            l, r = i,i
            while l <= r:
                if  s[l] != s[r]:
                    break
                
                if r-l +1 > len(an):
                    an = s[l:r+1]
                
                l -= 1
                r += 1
            l, r = i,i +1
            while l <= r:
                if s[l] != s[r]:
                    break
                if r-l +1 > len(an):
                    an = s[l:r+1]
                
                l -= 1
                r += 1
        return an

