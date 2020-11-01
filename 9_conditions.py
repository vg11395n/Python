# if-else
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day!!!")

# Task #1:  Price of a house is $1M
#           If buyer has good credit,
#               they need to put down 10%
#           otherwise
#               they need to put down 20%

print('The price of the house of $1M!!!')
credit = input('What is your credit score:')
income = input('What is your annual income:')
criminal_record = False
credit = int(credit)
income = int(income)

ten_perc = float((1000000 * 10)/100)
twenty_perc = float((1000000 * 20)/100)

if credit >= 600 and income > 70000 and not criminal_record:
    print('Then you need to put down 10% of $1M:', ten_perc)
    print('You are also eligible for loan!!')
else:
    print('Then you need to put down 20% of $1M:', twenty_perc)


weight = float(input('Weight: '))
lb_or_kg = input('''(L)bs or (K)gs: ''')
if lb_or_kg.upper() == 'L':
    weight_kg = float(weight) * 0.453592
    print(f'You are {weight_kg} kilos')
else:
    weight_lb = float(weight) / 0.453592
    print(f'You are {weight_lb} pounds')

