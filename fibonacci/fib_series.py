# Input for the range of Fibonacci series
nrange = int(input("Enter range of Fibonacci Series:"))

# Initializing the first two numbers of the Fibonacci sequence
n1 = 0
n2 = 1
count = 0

# Check if the input is a valid positive number
if nrange <= 0:
    print(f"Please Enter Positive Range")  
    # Negative numbers are invalid for Fibonacci series

# Special case where the range is 1
elif nrange == 1:
    print(f"Fibonacci Series for Range {nrange} is :\n",n1)  
    # Print only the first Fibonacci number

# General case for ranges greater than 1
else:
    print(f"Fibonacci Series for Range {nrange} is :")
    
    # Loop to generate the Fibonacci sequence up to the specified range
    while count < nrange:
        print(f"{n1} |",end=" ")
        # Print the current Fibonacci number with separator
        nth = n1 + n2  
        # Calculate the next Fibonacci number
        n1 = n2  
        # Update n1 to the next number in the series
        n2 = nth  
        # Update n2 to the next number in the series
        count += 1  
        # Increment the count to track the number of terms printed


#Output
# Enter range of Fibonacci Series:0
# Please Enter Positive Range

# Enter range of Fibonacci Series:1
# Fibonacci Series for Range 1 is :
#  0

# Enter range of Fibonacci Series:10
# Fibonacci Series for Range 10 is :
# 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 