
def get_common_elements(a1, b1, a2, b2, L, R):
    common_elements = []
    for i in range(L, R+1):
        if i == a1*k + b1 and i == a2*l + b2:
            common_elements.append(i)
    return len(common_elements)

def main():
    a1, b1, a2, b2, L, R = map(int, input().split())
    print(get_common_elements(a1, b1, a2, b2, L, R))

if __name__ == '__main__':
    main()

