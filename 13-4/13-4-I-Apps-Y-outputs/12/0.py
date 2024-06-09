
def get_input():
    return int(input())

def is_valid_input(L):
    return 1 <= L <= 1000

def get_volume(L):
    # Initialize variables
    a = b = c = 0
    volume = 0
    
    # Iterate through all possible combinations of a, b, and c
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            for k in range(1, L + 1):
                if i + j + k == L:
                    volume = max(volume, i * j * k)
    
    return volume

def main():
    L = get_input()
    if is_valid_input(L):
        print(get_volume(L))
    else:
        print("Invalid input")

if __name__ == '__main__':
    main()

