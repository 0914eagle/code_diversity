
n = int(input())
array = list(map(int, input().split()))

if n % 2 == 0:
    print(sum(abs(x) for x in array))
else:
    min_abs = min(abs(x) for x in array)
    count_negatives = sum(1 for x in array if x < 0)
    
    if count_negatives % 2 == 0:
        print(sum(abs(x) for x in array))
    else:
        print(sum(abs(x) for x in array) - 2 * min_abs)
