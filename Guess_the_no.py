 # Mini Project "Guess the number" 
import random
import math
#import simplegui #in CodeSkulptor
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# initialize global variables used in your code
limit = 100
secret_number = random.randrange(0, 100)
max_guess =math.ceil(math.log(limit+1,2))

# define event handlers for control panel
    
def range100():
    global secret_number, max_guess, limit
    secret_number = random.randrange(0, 100)  
    max_guess = math.ceil(math.log(limit+1,2))
    print "Let's try a new secret number, ranging from 0 to 100!"
    print "You have", int(max_guess),"guesses remaining.\n"
    # button that changes range to range [0,100) and restarts

def range1000():
    global secret_number, max_guess, limit
    secret_number = random.randrange(0, 1000)
    limit=1000
    max_guess = math.ceil(math.log(limit+1,2))
    print "Let's try a new secret number, ranging from 0 to 1000!"
    print "You have", int(max_guess),"guesses remaining.\n"
    # button that changes range to range [0,1000) and restarts

def get_input(guess):
    # main game logic goes here 
    global max_guess, limit,secret_number
    max_guess -= 1 
    if int(max_guess) > 0 :
        if int(guess) == secret_number and limit==100:
            print guess, "is correct. You won congratulation! \n "
            max_guess = math.ceil(math.log(limit+1,2))
            secret_number = random.randint(0,limit)
            range100()
     
        elif int(guess) == secret_number and limit==1000:
            print guess, "is correct. You won congratulation! \n"
            max_guess = math.ceil(math.log(limit+1,2))
            secret_number = random.randint(0,limit)
            range1000()
    
        elif int(guess) > secret_number:
            print "Guess is " + guess + ". Try Lower."
            print "You have", int(max_guess),"guesses remaining."
        else: 
            print "Guess is " + guess +". Try Higher."
            print "You have", int(max_guess),"guesses remaining."
    
    else:
        
        if int(guess) == secret_number :
            if limit==100:
                print guess, "is correct. You won congratulation! \n "
                max_guess = math.ceil(math.log(limit+1,2))
                secret_number = random.randint(0,limit)
                range100()
     
            else:
                print guess, "is correct. You won congratulation! \n"
                max_guess = math.ceil(math.log(limit+1,2))
                secret_number = random.randint(0,limit)
                range1000()
           
        else:
            if limit==1000:
                print "You Lose. The Secret Number was ", secret_number, " \n"
                max_guess = math.ceil(math.log(limit+1,2))
                secret_number = random.randint(0,limit)
                range1000()
            
            else :
                print "You Lose. The Secret Number was ", secret_number," \n"
                max_guess = math.ceil(math.log(limit+1,2))
                secret_number = random.randint(0,limit)
                range100()
    
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements
game_100 = frame.add_button("Range: 0 - 100", range100)
game_1000 = frame.add_button("Range: 0 - 1000", range1000)
inpt = frame.add_input("Enter guess", get_input, 100)

# start frame
frame.start()
