class Solution:
    def isPalindrome(self, s: str) -> bool:
        #brute force, clean string then compare it to reverse

        clean_str = ""
        
        for c in s:
            if c.isalnum():
                clean_str += c.lower()
        
        return clean_str == clean_str[::-1]

        