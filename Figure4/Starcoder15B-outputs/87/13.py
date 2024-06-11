def get_row(lst, x):
    
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    return result

print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1))
print(get_row([], 1))
print(get_row([[], [1], [1, 2, 3]], 3))
/python/python_codewars/01_8kyu/003_sum_of_positive.py
