
def get_max_files(x, y):
    n = len(x)
    m = len(y)
    if n != m:
        return 0
    
    x_sum = sum(x)
    y_sum = sum(y)
    if x_sum != y_sum:
        return 0
    
    files = []
    for i in range(n):
        files.append([x[i], y[i]])
    
    files.sort(key=lambda x: x[0])
    
    max_files = 0
    curr_sum = 0
    for file in files:
        curr_sum += file[0]
        if curr_sum > file[1]:
            return 0
        if curr_sum == file[1]:
            max_files += 1
            curr_sum = 0
    
    return max_files

