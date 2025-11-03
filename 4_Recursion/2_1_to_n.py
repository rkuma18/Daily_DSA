# Print a number from 1 to 4 by using recursion

N = 4
# without recursion
def one_to_n(N):
    for i in range(1, N+1):
        print(i)

#one_to_n(N)  


# with recursion
def rec_one_to_n(n, current=1):
    if current > n:
        return
    print(current)
    rec_one_to_n(n, current + 1)


rec_one_to_n(N)

