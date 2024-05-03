import math
Num = int(input("  Enter a number: "))
Num1 = int(input("Enter another number: "))


'''adding more numbers'''
Num3 = str(input("do you want to add another number? (Yes/No)  "))
yes = 'yes'
no = 'no'
if Num3 == yes:
    global Num4
    Num4 = int(input('Enter the next number: '))
    for ans in Num3:
        Num2 =  str(input('Do you want to add a number again? (yes/no): '))
        if Num2 == yes:
            global Num5
            Num5 = int(input("Enter the next number: "))
        elif Num2 == no:
            print('Now you can choose an operator.')
            break
        else:
            print('You can only answer yes or no')
        print()
elif Num3 == no:
    print('Now you can choose an operator.')
else:
    print('You can only answer yes or no')


'''Choosing operators'''
op = (input('Choose an operator (+,-,*,/): '))



if op == '+' and Num3 == no:
    print('The sum of {Num}, {Num1}, is ', Num + Num1)
elif op == '-' and Num3 == no:
    print('The difference between', Num, Num1, ' is ', Num - Num1)
elif op == '*' and Num3 == no:
    print('When we multiply ', Num, ' with ', Num1, ' the answer is ', Num * Num1)
elif op == '/' and Num3 == no:
    print('When we divide ', Num, ' by ', Num1, ' the answer is ', Num / Num1)




elif op == '+' and Num3 == yes and Num2 == no:
    print('The sum of', Num, Num1, 'and', Num4, 'is', Num + Num1 + Num4)
elif op == '-' and Num3 == yes and Num2 == no:
    print('The difference between', Num, Num1, 'and', Num4, 'is', Num - Num1)
elif op == '*' and Num3 == yes and Num2 == no:
    print('When we multiply', Num, Num1, 'and', Num4, 'the answer is', Num * Num1 * Num4)
elif op == '/' and Num3 == yes and Num2 == no:
    print('When we divide', Num, Num1, 'and', Num4, 'the answer is', Num / Num1 / Num4)




elif op == '+' and Num3 == yes and Num2 == yes:
    print('The sum of', Num, Num1, Num4, 'and', Num5, 'is', Num + Num1 + Num4 + Num5)
elif op == '-' and Num3 == yes and Num2 == yes:
    print('The difference between', Num, Num1, Num4, 'and', Num5, 'is', Num - Num1)
elif op == '*' and Num3 == yes and Num2 == yes:
    print('When we multiply', Num, Num1, Num4, 'and', Num5, 'the answer is', Num * Num1 * Num4)
elif op == '/' and Num3 == yes and Num2 == yes:
    print('When we divide', Num, Num1, Num4, 'and', Num5, 'the answer is', Num / Num1 / Num4)