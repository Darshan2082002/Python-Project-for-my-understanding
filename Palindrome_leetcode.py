



class Solution:
    def isPalindrome(self, x: int) -> bool:
        x3=str(x)
        x2=x3[::-1]
        

        if x3==x2:
            return True
        else:
            return False
        