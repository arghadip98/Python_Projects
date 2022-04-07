num = int(input("Enter any number: "))
num1 , num2 = 0 , 1
sum = 0
if(num<=0):
    print('Enter a number which will be greater than 0')
else:
    for i in range(0 , num):
        print(sum, end = ' ')
        num1 = num2
        num2 = sum
        sum = num1 + num2