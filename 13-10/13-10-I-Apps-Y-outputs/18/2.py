
def get_throw_scores(target_score):
    throw_scores = []
    for i in range(1, 21):
        if target_score == i:
            throw_scores.append(f"single {i}")
        elif target_score == 2*i:
            throw_scores.append(f"double {i}")
        elif target_score == 3*i:
            throw_scores.append(f"triple {i}")
    return throw_scores

def main():
    target_score = int(input("Enter target score: "))
    throw_scores = get_throw_scores(target_score)
    if throw_scores:
        for throw_score in throw_scores:
            print(throw_score)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()

