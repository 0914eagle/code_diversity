
def get_scores(target_score):
    scores = []
    for i in range(1, 21):
        if i * 3 == target_score:
            scores.append(f"triple {i}")
        elif i * 2 == target_score:
            scores.append(f"double {i}")
        elif i == target_score:
            scores.append(f"single {i}")
    
    return scores

def main():
    target_score = int(input("Enter target score: "))
    scores = get_scores(target_score)
    if scores:
        for score in scores:
            print(score)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()

