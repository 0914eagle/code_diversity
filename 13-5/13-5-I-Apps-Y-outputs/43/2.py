
def get_unique_outcome(rolls):
    unique_rolls = set(rolls)
    if len(unique_rolls) == 1:
        return "none"
    else:
        return str(max(rolls))

def get_winner_index(rolls):
    unique_rolls = set(rolls)
    if len(unique_rolls) == 1:
        return "none"
    else:
        return str(rolls.index(max(unique_rolls)) + 1)

if __name__ == '__main__':
    n = int(input())
    rolls = list(map(int, input().split()))
    print(get_winner_index(rolls))

