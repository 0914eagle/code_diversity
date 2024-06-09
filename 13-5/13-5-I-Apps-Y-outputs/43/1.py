
def get_unique_outcome(outcomes):
    unique_outcomes = set(outcomes)
    if len(unique_outcomes) == 1:
        return "none"
    else:
        return str(outcomes.index(max(unique_outcomes)) + 1)

def main():
    n = int(input())
    outcomes = list(map(int, input().split()))
    print(get_unique_outcome(outcomes))

if __name__ == '__main__':
    main()

