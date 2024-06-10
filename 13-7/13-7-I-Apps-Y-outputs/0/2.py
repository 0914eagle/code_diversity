
def get_possible_answers(b, d, c, l):
    possible_answers = []
    for b_count in range(1, 101):
        if b_count * b > l:
            break
        d_count = (l - b_count * b) // d
        if d_count * d + b_count * b != l:
            continue
        for c_count in range(0, 101):
            if d_count + c_count > 100:
                break
            if b_count + d_count + c_count != 100:
                continue
            possible_answers.append((b_count, d_count, c_count))
    return possible_answers

def main():
    b, d, c, l = map(int, input().split())
    possible_answers = get_possible_answers(b, d, c, l)
    if not possible_answers:
        print("impossible")
    else:
        for b_count, d_count, c_count in possible_answers:
            print(f"{b_count} {d_count} {c_count}")

if __name__ == '__main__':
    main()

