# Write your code here :-)
import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for question in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#' + str(question) + ': ' + str(num1) + ' x ' + str(num2) + ' = '
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*','Incorrect!')])
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
    print('Score: ' + str(correctAnswers) + ' / ' + str(numberOfQuestions))
