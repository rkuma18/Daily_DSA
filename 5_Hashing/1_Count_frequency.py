numbers = [1, 2, 2, 3, 1, 4, 2, 3, 1]
def freq(number):
    count ={}
    # precomputing/prehashing
    for num in number:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for key,value in count.items():
        print(f'{key} appears {value} times')
    

freq(numbers)