import time
# Addition
def a():
    print("'Addition'")
    total = 0
    count = 0
    num = float(input('Enter the first number for addition: '))
    while num != 0:
            total += num
            num = float(input('Enter the another number for addition or 0 to compute the current calculations: '))
            count+=1

    return [f"Answer: {total}", f"total number of inputs given: {count}"]

# Subtraction
def s():
    print("'Subtraction'")
    total = 0
    count = 0
    num = float(input('Enter the first number you want to subtract: '))
    while num!=0:
        total = total + num
        num = -(float(input('Enter the another number for subtraction or 0 to compute the current calculations: ')))
        count+=1
        if num ==0:
         print("Thanks")
         break
    return [f"Answer: {total}", f"total number of inputs given: {count}"]

# Multiplication
def m():
    print("'Multiplication'")
    total = 1
    count = 0
    num = float(input('Enter the first number you want to multiply: '))
    while num!=0:
        total = total * num
        num = float(input('Enter the another number for multiplication or 0 to compute the current calculations: '))
        count+=1
    return [f"Answer: {total}", f"total number of inputs given: {count}"]


# Divide
def d():
    print("'Divide'")
    total = 1
    count = 0
    num = float(input('Enter the first number you want to divide: '))
    while num != 0:
        num = float(input('Enter the another number to divide or 1 to compute the current calculations: '))
        count += 1
        if num == 1:
            break
    return [f"Answer: {total}", f"total number of inputs given: {count}"]

run = input("Please select from the following operations: \n"
            "Press 'a' for Addition\n"
            "Press 's' for Subtraction\n"
            "Press 'm' for Multiplication\n"
            "Press 'd' for Divide\n"
            "Press 'q' to quit\n")
#
# if run!=['a','s','m','d','q']:
#   print("Please enter a valid input")
#   run = input("Please select from the following operations: \n"
#                     "Press 'a' for Addition\n"
#                     "Press 's' for Subtraction\n"
#                     "Press 'm' for Multiplication\n"
#                     "Press 'd' for Divide\n"
#                     "Press 'q' to quit\n")

while run not in ['a', 's', 'm', 'd', 'q']:
    print("Invalid input")
    run = input("Please select from the following operations: \n"
                "Press 'a' for Addition\n"
                "Press 's' for Subtraction\n"
                "Press 'm' for Multiplication\n"
                "Press 'd' for Divide\n"
                "Press 'q' to quit\n")
else:
    if run == 'a':
        print(a())
        time.sleep(1)
        print('Thank you for using calculator')
        # break
    elif run == 's':
        print(s())
        time.sleep(1)
        print('Thank you for using calculator')
        # break
    elif run == 'm':
        print(m())
        time.sleep(1)
        print('Thank you for using calculator')
        # break
    elif run == 'd':
        print(d())
        time.sleep(1)
        print('Thank you for using calculator')
        # break
    elif run == 'q':
        time.sleep(1)
        print('Thank you for using calculator')
        # break
