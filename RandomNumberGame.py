#Number guessing game in Python
import random as r
import secrets
import json
def Guess():
   a = r.randint(1, 10)
   srtkey = secrets.token_hex(16)
   data = {"users":{"key":srtkey, "Answer": a}}
   json.dumps(data)
   return a

RandG = Guess()

def Pick(num):
    return num

state = True
count = 0
while state:
    a = input("Guess a number between 1 -10 ")
    print(Pick(a))
    if int(Pick(a)) == int(RandG):
        print("WIN")

        state = False
    else:
        count = count +1
        print("Lose")
        if count == 5:
            state = False
            print("You exhausted 5 chances")