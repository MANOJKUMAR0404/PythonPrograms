#type 1
num = input("Enter a Number : ")
rev = num[::-1]
if num == rev :
    print(f"{num} is Palindrome")
else:
    print(f"{num} is not an Palindrome")


#type 2
num2 = int(input("Enter a Number : "))
temp = num2
rev = 0
while temp > 0 :
    remainder = temp % 10
    rev = (rev * 10) + remainder
    temp = temp // 10
if num2 == rev :
    print(f"{num2} is Palindrome")
else :
    print(f"{num2} is not an Palindrome")

