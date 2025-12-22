"""
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.

"""


class Solution:
    def checkStatus(self, a, b, flag):
        # code here
         if ((a*b<0 and flag==False)or (((a<0)and(b<0)and flag==True))):
             return True 
         else:
             return False
            
            
             return True if ((a*b<0)and not flag) or((a<0)and(b<0)and flag) else False