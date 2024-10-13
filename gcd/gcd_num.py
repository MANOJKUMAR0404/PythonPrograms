def gcd(a, b):
    # Base case: if the first number is 0, return the second number
    if (a == 0):
        return b
    # Base case: if the second number is 0, return the first number
    if (b == 0):
        return a

    # If both numbers are equal, return either of them (since GCD is the number itself)
    if (a == b):
        return a

    # If the first number is greater, recursively call gcd with (a - b) and b
    if (a > b):
        return gcd(a - b, b)
    
    # If the second number is greater, recursively call gcd with a and (b - a)
    return gcd(a, b - a)

# Taking user input for the two numbers
first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))

# If the GCD is found, print the result
if(gcd(first_num, second_num)):
    print('GCD of', first_num, 'and', second_num, 'is', gcd(first_num, second_num))
else:
    print('not found')


#output
# Enter First Number: 81
# Enter Second Number: 108
# GCD of 81 and 108 is 27

# Enter First Number: 12
# Enter Second Number: 18
# GCD of 12 and 18 is 6

# Enter First Number: 10
# Enter Second Number: 20
# GCD of 10 and 20 is 10
