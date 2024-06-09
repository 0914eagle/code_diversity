
def is_increasing(names):
    return all(names[i] < names[i+1] for i in range(len(names)-1))

def is_decreasing(names):
    return all(names[i] > names[i+1] for i in range(len(names)-1))

def is_neither(names):
    return not (is_increasing(names) or is_decreasing(names))

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

