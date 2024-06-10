
def is_increasing(names):
    return sorted(names) == names

def is_decreasing(names):
    return sorted(names, reverse=True) == names

def solve(names):
    if is_increasing(names):
        return "INCREASING"
    elif is_decreasing(names):
        return "DECREASING"
    else:
        return "NEITHER"

if __name__ == '__main__':
    num_names = int(input())
    names = []
    for i in range(num_names):
        names.append(input())
    print(solve(names))

