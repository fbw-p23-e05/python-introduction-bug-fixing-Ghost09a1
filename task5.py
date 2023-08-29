x = int(input("First number: "))  # Convert  
y = int(input("Second number: "))  # Convert 
z = int(input("Third number: "))  # Convert 

if x == y or y == z:  # '==' for equality comparison
    result = 0
else:
    result = x + y + z  #  'result' instead 'sum'
    
print("Calculated sum is", result)  # Corrected the variable name 'sum' to 'result'
