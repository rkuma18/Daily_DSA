def n_name(name, count, N):
    if count == N:
        return 'Done'
    print(name)
    result = n_name(name, count + 1, N)
    return result

    
N = 5
name = "Roushan"
n_name(name,0, N)