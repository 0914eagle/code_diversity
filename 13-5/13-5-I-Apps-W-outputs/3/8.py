
def get_input():
    return map(int, input().split())

def get_common_elements(a1, b1, a2, b2, L, R):
    common_elements = set()
    for k in range(L//a1):
        for l in range(L//a2):
            if a1*k + b1 == a2*l + b2:
                common_elements.add(a1*k + b1)
    return len(common_elements)

def main():
    a1, b1, a2, b2, L, R = get_input()
    print(get_common_elements(a1, b1, a2, b2, L, R))

if __name__ == '__main__':
    main()

