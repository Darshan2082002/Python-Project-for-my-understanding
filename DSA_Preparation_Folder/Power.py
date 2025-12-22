def isPowerOfTwo(self, n: int) -> bool:
        if (n>0 and(n&(n-1))==0):# this use bit manipulation 
            return True
        else:
            return False
    
if __name__=="__main__":
    print(isPowerOfTwo(6))