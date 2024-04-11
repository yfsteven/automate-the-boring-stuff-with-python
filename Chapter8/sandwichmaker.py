# Write your code here :-)
import pyinputplus as pyip

while True:
    prices = {'mayo': 0.50, 'mustard': 0.25, 'lettuce': 0.35, 'tomato': 0.75,'wheat': 4.30, 'white': 3.20, 'sourdough': 5.00, 'chicken': 2.00, 'turkey':3.50,'ham':2.45,'tofu':1.40,'cheddar':1.00,'swiss':2.00,'mozzarella':2.20}
    bread_order = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    protein_order = pyip.inputMenu(['chicken','turkey','ham','tofu'])
    cheese_prompt = 'Do you want cheese with that?\n'
    extra_prompt = 'Anything else?\n'
    cheese = 0
    extra = 0
    cheese_response = pyip.inputYesNo(cheese_prompt)
    if cheese_response == 'yes':
        cheese_order = pyip.inputMenu(['cheddar','swiss','mozzarella'])
        cheese = prices[cheese_order]
    extra_response = pyip.inputYesNo(extra_prompt)
    if extra_response == 'yes':
        extra_packet = pyip.inputMenu(['mayo','mustard','lettuce','tomato'])
        extra = prices[extra_packet]
    number_prompt = 'How many sandwiches you want?\n'
    number_sandwiches = pyip.inputInt(number_prompt,min=1)
    total_cost = prices[bread_order] + prices[protein_order] + cheese
    print('$' + str('%.2f' % (total_cost * number_sandwiches)))
    break
