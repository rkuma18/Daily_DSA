# Print a number from 4 to 1 by using recursion

N = 4

def n_to_one(N):
    for i in range(N, 0, -1):
        print(i)
#n_to_one(N)



def rec_n_to_one(n):
    if n == 0:
        return
    print(n)
    rec_n_to_one(n - 1)


rec_n_to_one(N)

