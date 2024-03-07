# Write your code here :-)
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    contain_ht = []
    streak = 1
    for i in range(100):
        contain_ht.append(random.randint(0, 1))

    for k in range(1, len(contain_ht)):
        if contain_ht[k] == contain_ht[k-1]:
            streak += 1
        else:
            streak = 1
        if streak == 6:
            numberOfStreaks += 1
            break
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
