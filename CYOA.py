#This is a choose your own adventure game
#Good luck!
import sys

print('Hello, adventurer. What is your name?')
name = input()

print('' + name + ', I have a quest for you. Will you accept? Yes or no?')
answer = input()

if answer == ('yes','Yes'):
    print('Wonderful! Great news. This quest will require wits and bravery. Yes I know, in this economy. First, ' + name + ', how old are you? For... insurance purposes.')
    age = int(input())
elif answer == ('no' or 'No'):
    print('Oh, okay. Man I really did not expect that. Wow, uhm okay then I guess. I have to go, uh, figure this out now. Bye then I guess. Jeeze.')
    sys.exit('Guess he is on his own. Jerk.')
