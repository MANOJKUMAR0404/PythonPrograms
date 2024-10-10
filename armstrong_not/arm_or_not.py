#type 1
num  = input("Enter an Number:")
arm_no = 0
if int(num) < 10:
    print(f"{num} is an Armstrong Number")
for i in num:
    arm_no+=int(i)**3
if int(num) == arm_no:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


#Output

# Enter an Number: 408
# 408 is an Armstrong Number
# Enter an Number: 370
# 408 is an Armstrong Number
# Enter an Number: 199
# 408 is not an Armstrong Number

# type 2
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")