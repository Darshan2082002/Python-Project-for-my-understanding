import random as rd

def word():
    words=["innovation", "strategy", "adventure", "nebula", "quantum"]
    a=rd.choice(words)
    count=0
    print("Word Guessing Game!!!")
    while True:
        try:
            n=str(input("Enter thw Word !!!!"))
            count+=1
        except:
            print("Try again ")
            continue
        if n==a:
            print(" Greate you found it ")
            break
        
        else:
            print('Try again !!!')



word()