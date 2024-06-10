
def is_increasing(names):
    return all(names[i] <= names[i+1] for i in range(len(names)-1))

def is_decreasing(names):
    return all(names[i] >= names[i+1] for i in range(len(names)-1))

def get_order(names):
    if is_increasing(names):
        return "INCREASING"
    elif is_decreasing(names):
        return "DECREASING"
    else:
        return "NEITHER"

if __name__ == '__main__':
    num_names = int(input())
    names = []
    for _ in range(num_names):
        names.append(input())
    print(get_order(names))

