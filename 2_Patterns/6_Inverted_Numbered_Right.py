user = input("Enter the Inverted Numbered Right size: ")
number = int(user)
for i in range(number):
    for j in range(1,number-i+1):
        print(j, end=" ")
    print()