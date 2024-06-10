
def get_sorted_names(names):
    return sorted(names)

def get_sorted_names_reverse(names):
    return sorted(names, reverse=True)

def check_order(names):
    sorted_names = get_sorted_names(names)
    sorted_names_reverse = get_sorted_names_reverse(names)
    if names == sorted_names:
        return "INCREASING"
    elif names == sorted_names_reverse:
        return "DECREASING"
    else:
        return "NEITHER"

if __name__ == '__main__':
    num_names = int(input())
    names = []
    for _ in range(num_names):
        names.append(input())
    print(check_order(names))

