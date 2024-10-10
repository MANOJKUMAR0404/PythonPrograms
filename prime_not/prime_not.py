num = int(input("Enter an Number:"))
flag = False
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
elif num == 0 or num == 1:
    flag = True
if flag:
    print(f"{num} is Not an Prime Number")
else:
    print(f"{num} is an Prime Number")