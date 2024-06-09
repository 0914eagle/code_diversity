
def get_last_child(n, m, a):
    line = list(range(1, n+1))
    while line:
        for i in range(m):
            if line[0] <= a[line[0]-1]:
                line.append(line.pop(0))
            else:
                line.pop(0)
                break
    return line[-1]

