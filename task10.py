x = int(input("First number: "))  # Convert integer
y = int(input("Second number: "))  # Convert integer

if x % y == 0:  # Use '%' for modulo and '==' 
    print("First number is divisible by second number, result =", x // y)
elif y % x == 0:  # Use '%' for modulo and '==' 
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisible!")
