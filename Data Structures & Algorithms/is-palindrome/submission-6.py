class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set l,r finsh loop when they cross and only move both if valid and only move 1 if non-alpha
        l,r = 0, len(s) - 1

        while l<r:
            while l<r and not s[r].isalnum():
                r -= 1
            while l<r and not s[l].isalnum():
                l+= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
        