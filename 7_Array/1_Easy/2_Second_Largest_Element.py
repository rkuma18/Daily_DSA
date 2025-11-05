def sortSecArr(arr,n):
    if n == 0 and n == 1:
        return -1
    
    arr.sort()
    small = arr[0]
    last_Sec = arr[n-2]

    print('Second Largest element in a array:', last_Sec)
    print('Smallest element in a array:', small)    



arr= [8,10,5,7,9]
n = len(arr)
sortSecArr(arr,n)
