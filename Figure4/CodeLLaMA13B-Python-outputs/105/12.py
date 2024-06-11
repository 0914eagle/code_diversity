def by_length(arr):
    
    if len(arr) == 0:
        return []
    else:
        arr.sort()
        arr.reverse()
        for i in range(len(arr)):
            if arr[i] < 1 or arr[i] > 9:
                arr.remove(arr[i])
        arr = [str(i) for i in arr]
        for i in range(len(arr)):
            if arr[i] == '1':
                arr[i] = 'One'
            elif arr[i] == '2':
                arr[i] = 'Two'
            elif arr[i] == '3':
                arr[i] = 'Three'
            elif arr[i] == '4':
                arr[i] = 'Four'
            elif arr[i] == '5':
                arr[i] = 'Five'
            elif arr[i] == '6':
                arr[i] = 'Six'
            elif arr[i] == '7':
                arr[i] = 'Seven'
            elif arr[i] == '8':
                arr[i] = 'Eight'
            elif arr[i] == '9':
                arr[i] = 'Nine'
        return arr


