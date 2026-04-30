import random as rd 

def random_gen():
    a=rd.randint(1,100)
    count=0

    while True:
        try:
            n=int(input("Enter your guess(1-100):"))
            count +=1
        except ValueError:
            print("Invalid input! please enter a valid interger.")
            continue

        if n == a:
            print(f"correctg ! It took you {count} attempts to predict the  number")
            break
        elif n>a:
            print(" Number is too high ! Try again \n")
        else:
            print(" Number is too low!  Try again \n")


            




game=random_gen()