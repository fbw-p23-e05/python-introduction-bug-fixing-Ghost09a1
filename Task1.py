three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5 # coz buzz 5 times
max_num = 100
   
for i in range(1, max_num):  # max_number to max_num
    if i % num1 == 0 and i % num2 == 0:  # Check for multiples of both num1 and num2 first
        print(i, three_mul + five_mul)
    elif i % num1 == 0:
        print(i, three_mul)
    elif i % num2 == 0:
        print(i, five_mul)
    else:
        print(i)  # Print the number itself if it's not a multiple of 3 or 5