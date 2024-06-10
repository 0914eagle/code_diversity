
def get_target_score():
    n = int(input())
    return n

def get_throw_scores(n):
    throw_scores = []
    for i in range(1, 21):
        if i * 3 <= n:
            throw_scores.append(f"triple {i}")
        if i * 2 <= n:
            throw_scores.append(f"double {i}")
        if i <= n:
            throw_scores.append(f"single {i}")
    return throw_scores

def main():
    n = get_target_score()
    throw_scores = get_throw_scores(n)
    print("\n".join(throw_scores))

if __name__ == '__main__':
    main()

