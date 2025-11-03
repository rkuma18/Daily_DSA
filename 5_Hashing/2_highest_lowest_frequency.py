numbers = [1, 2, 2, 3, 1, 4, 2, 3, 1, 2]

def freq(number):
    count = {}
    # Precomputing / Prehashing
    for num in number:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    # Find number with highest and lowest frequency
    max_freq = max(count.values())
    min_freq = min(count.values())
   
    # Get numbers having those frequencies
    highest = [key for key, value in count.items() if value == max_freq]
    lowest = [key for key, value in count.items() if value == min_freq]

    print(f'Highest frequency ({max_freq}) → {highest}')
    print(f'Lowest frequency ({min_freq}) → {lowest}')

freq(numbers)
