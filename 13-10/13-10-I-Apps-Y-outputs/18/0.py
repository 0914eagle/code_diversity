
def get_throw_scores(target_score):
    scores = []
    for i in range(1, 21):
        if i * 3 == target_score:
            scores.append(f"triple {i}")
        elif i * 2 == target_score:
            scores.append(f"double {i}")
        elif i == target_score:
            scores.append(f"single {i}")
    
    return scores if scores else "impossible"

def main():
    target_score = int(input("Enter target score: "))
    print(get_throw_scores(target_score))

if __name__ == '__main__':
    main()

