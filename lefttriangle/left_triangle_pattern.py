# get input for size of triangle
range_num = int(input("Enter Size of Triangle: "))

# loop to handle rows
for i in range(range_num):
    
    # loop to print stars in each row
    for j in range(i+1):
        print("*", end=" ")  # print stars in same line
    
    print("\n")  # move to next line after each row


# Output

# Enter Size of Triangle: 5
# *         

# * *       

# * * *     

# * * * *   

# * * * * * 