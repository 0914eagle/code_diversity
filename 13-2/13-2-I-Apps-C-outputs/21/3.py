
def f1(n, a):
    # Find the index of the number that is not sorted
    index = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            index = i
            break
    
    # Find the digit that can be changed to make the number not sorted
    digit = 0
    for i in range(len(str(a[index]))):
        if str(a[index])[i] != str(a[index-1])[i]:
            digit = i
            break
    
    # Change the digit to make the number not sorted
    b = list(str(a[index]))
    b[digit] = str(a[index-1])[digit]
    b = int("".join(b))
    
    return b

def f2(n, a):
    # Check if the list is already sorted
    if all(a[i+1] >= a[i] for i in range(n-1)):
        return "impossible"
    
    # Find the index of the number that is not sorted
    index = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            index = i
            break
    
    # Find the digit that can be changed to make the number not sorted
    digit = 0
    for i in range(len(str(a[index]))):
        if str(a[index])[i] != str(a[index-1])[i]:
            digit = i
            break
    
    # Change the digit to make the number not sorted
    b = list(str(a[index]))
    b[digit] = str(a[index-1])[digit]
    b = int("".join(b))
    
    return b

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f2(n, a))

