'''
elif can be used multiple times
both elif and esle are idented the same as the original if
when codding alway allways use variable names that make sence to you!!!
this helps you solve problems by understanding exactly what each thing is
range(0,2) gives range of numbers from 0 to 2
the first pic in a list of any kind is 0 not 1
'''

from random import randint
You = 0
Comp = 0
def RockPaperScissors(shoot):

# creates options in game
    List = ['rock','paper','scissors']
# pics rock paper or scissors
    rand_pic = List[randint(0,2)]
    global You,Comp

    if rand_pic == shoot:
        print "%s!..... Again!!" %rand_pic

    elif rand_pic == 'rock' and shoot == 'scissors':
        print "%s I win!"%rand_pic
        Comp = Comp + 1

    elif rand_pic == 'paper' and shoot == 'rock':
        print "%s I win!"%rand_pic
        Comp = Comp + 1

    elif rand_pic == 'scissors' and shoot == 'paper':
        print "%s I win!"%rand_pic
        Comp = Comp + 1

    else:
        print '%s.... you have bested me'%rand_pic
        You = You + 1

guess = raw_input("Rock Paper Scissors Shoot!:  ")

RockPaperScissors(guess)

print "you:%d computer:%d" %(You,Comp)
