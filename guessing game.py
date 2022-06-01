import random

print("welcome to my game")

number = input("enter a number? ")
if  number.isdigit():
    number = int(number)
    
    if number == 0:
        print("chose a number greater than 0")
        quit()
else:
        print("please enter a number!")
        quit()
        
number = random.randint(0,number)
guesses=0
        
while True:
        guesses += 1
        guess_number = input("guess a number! ")  
        
        if guess_number.isdigit():
            guess_number = int(guess_number)
        else:
            print ("enter a number")
            continue
            
           
        if guess_number == number:
             print ("you got it")
             break
             
        elif guess_number > number:
            print("number too high")    
        else:
            print("number too low")
        
print("you got it in", guesses, "guesses")
