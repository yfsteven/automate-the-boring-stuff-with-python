import ezgmail, random

emails = ['python@gmail.com', 'fake@gmail.com']

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

for email in emails:
    randomChore = random.choice(chores)
    chores.remove(randomChore)    # this chore is now taken, so remove it
    ezgmail.send(email, 'Chore Assignment', f'Your responsibility is {randomChore}')
