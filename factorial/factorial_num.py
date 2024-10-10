# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter Any Number: "))
# Initialize the factorial variable to 1
factorial = 1
# Check if the number is negative
if num < 0:
    print(f"{num} - negative number not allowed")
# Check if the number is zero
elif num == 0:
    print(f"The Factorial of {num} is 1")
else:
    for i in range(1, num + 1):
        factorial *= i  # Multiply factorial by each number in the range
    print(f"The Factorial of {num} is {factorial}")




# Output

# Enter Any Number: 5
# The Factorial of 5 is 120

# Enter Any Number: 10
# The Factorial of 10 is 3628800

# Enter Any Number: -40
# -40 - negative number not allowed