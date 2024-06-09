
def get_max_rest(schedule):
    max_rest = 0
    current_rest = 0
    for i in range(len(schedule)):
        if schedule[i] == 0:
            current_rest += 1
        else:
            max_rest = max(max_rest, current_rest)
            current_rest = 0
    
    return max(max_rest, current_rest)

def main():
    n = int(input())
    schedule = list(map(int, input().split()))
    print(get_max_rest(schedule))

if __name__ == '__main__':
    main()

