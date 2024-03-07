# Write your code here :-)
def collatz(number):
    if number % 2 == 0: #even
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
try:
    while True:
        print('Input a number')
        user = int(input())
        if collatz(user) == 1:
            print('Escaping loop... done')
            break
except ValueError:
    print("Must be a number!")
