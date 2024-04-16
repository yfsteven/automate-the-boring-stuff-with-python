# 3 bugs fixed
# 1. Guess always has a string (heads or tails) opposed to Toss (0,1)
# 2. Incorrect variable name named guesss
# 3. During the second coin flip, toss has never been updated to a new value.
# So, it was always possible to pick the opposite 'guess' to win

import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of while loop: (%s%%) is'  % (guess))
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
logging.debug('End of while loop(%s%%)'  % (guess))
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Toss is (%s%%)'  % (toss))
if toss == 0 and guess == 'tails' or toss == 1 and guess == 'heads':
    print('You got it!')
    logging.debug('Guess is (%s%%)'  % (guess))
    logging.debug('Toss is (%d%%)'  % (toss))
else:
    print('Nope! Guess again!')
    guess = input()
    toss = random.randint(0, 1)
    if toss == 0 and guess == 'tails' or toss == 1 and guess == 'heads':
        logging.debug('Guess is (%s%%)'  % (guess))
        logging.debug('Toss is (%d%%)'  % (toss))
        print('You got it!')
    else:
        logging.debug('Guess is (%s%%)'  % (guess))
        logging.debug('Toss is (%d%%)'  % (toss))
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
