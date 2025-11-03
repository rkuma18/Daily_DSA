number = int(input("Enter the Inverted Star Pyramid size: "))

for i in range(number):
    # print leading spaces
    for j in range(number - i - 1):
        print("*", end=" ")
    # print stars
    for j in range(2 * i + 1):
        print(" ", end=" ")
    print()
