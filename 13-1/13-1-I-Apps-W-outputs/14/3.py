
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
    current_file = 0
    for i in range(n):
        current_file += files[i][0]
        if current_file == files[i][1]:
            max_files += 1
            current_file = 0
    
    return max_files

