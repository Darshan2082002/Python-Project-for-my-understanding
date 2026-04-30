from collections import Counter 
import random as rd
words=["darshan","tarshan","newyork","usa","uk"]
a=rd.choice(words)
while True:
    n=str(input("Enter the letter"))
    print(a)
    if a==n:
        print("you found it ")
        break


