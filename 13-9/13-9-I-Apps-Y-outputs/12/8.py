
def is_increasing_order(names):
    return sorted(names) == names

def is_decreasing_order(names):
    return sorted(names, reverse=True) == names

def get_order(names):
    if is_increasing_order(names):
        return "INCREASING"
    elif is_decreasing_order(names):
        return "DECREASING"
    else:
        return "NEITHER"

if __name__ == '__main__':
    num_names = int(input())
    names = []
    for _ in range(num_names):
        names.append(input())
    print(get_order(names))

