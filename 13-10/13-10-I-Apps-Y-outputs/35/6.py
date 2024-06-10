
def get_input():
    N = int(input())
    values = list(map(int, input().split()))
    return N, values

def get_max_value(values):
    if len(values) == 1:
        return values[0]
    
    max_value = 0
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            max_value = max(max_value, (values[i] + values[j]) / 2)
    
    return max_value

def main():
    N, values = get_input()
    print(get_max_value(values))

if __name__ == '__main__':
    main()

