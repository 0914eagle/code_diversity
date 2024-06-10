
def get_throw_scores(target_score):
    
    throw_scores = []
    for i in range(1, 21):
        if target_score % i == 0:
            throw_scores.append(i)
            target_score -= i
            if len(throw_scores) == 3:
                break
    if sum(throw_scores) == target_score:
        return throw_scores
    else:
        return "impossible"

def main():
    target_score = int(input("Enter target score: "))
    throw_scores = get_throw_scores(target_score)
    if throw_scores == "impossible":
        print("Impossible")
    else:
        for throw_score in throw_scores:
            print(f"triple {throw_score}")

if __name__ == '__main__':
    main()

