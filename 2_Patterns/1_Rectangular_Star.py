user = input("Enter the rectangular pattern size: ")
number = int(user)
for i in range(number):
    for j in range(number):
        print("*", end=" ")
    print()  # move to next line