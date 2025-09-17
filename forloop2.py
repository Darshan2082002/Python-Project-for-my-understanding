"""
You are given a string s, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.

Examples:

Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Input: s = "Geeks"
Output: Ges 

"""

def stringJumper(s):
    for i in range(len(s)):
        if i%2 ==0:
            print(s[i], end="")