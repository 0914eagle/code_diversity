
def is_increasing(names):
    return sorted(names) == names

def is_decreasing(names):
    return sorted(names, reverse=True) == names

def is_neither(names):
    return not is_increasing(names) and not is_decreasing(names)

def main():
    num_names = int(input())
    names = []
    for _ in range(num_names):
        names.append(input())
    if is_increasing(names):
        print("INCREASING")
    elif is_decreasing(names):
        print("DECREASING")
    else:
        print("NEITHER")

if __name__ == '__main__':
    main()

