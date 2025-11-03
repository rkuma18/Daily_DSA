user = input("Enter the rectangular pattern size: ")
number = int(user)
for i in range(number):
    for j in range(i,number):
        print("*", end=" ")
    print()