#Prime Number Checker
import time as t
print("Prime Checker Welcomes You!")
t.sleep(1.25)
print("You are the laziest person I've ever seen.")
t.sleep(0.80)
a= int(input("Enter a number to check = "))
print("Hold on.......")
b= False
if a==1:
    print("Your number", a ," is a prime number")
else:
    for i in range (2, a):
        if (i%a)==0:
            b = True
t.sleep(4)
if b:
    print("Your number", a ,"is not prime")
else:
    print("Your number", a ,"is prime")
t.sleep(2)
print("Next time do a bit hard work \nJust Kidding! \nThankYou for using me\nHave a great day!")
