x = input("Type your value: ")  # Input string

if x == "0":  # Use '==' 
    x = False  # 'False' instead of 'false'
elif x == "1":  # Use '==' 
    x = True  # Use 'True' instead of 'true'
else:
    pass

print("Your entered value is now", x)
