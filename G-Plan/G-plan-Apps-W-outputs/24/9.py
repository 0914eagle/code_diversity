
def check_relation(x, sign, answer, y):
    if sign == ">=":
        return y >= x if answer == "Y" else y < x
    elif sign == "<=":
        return y <= x if answer == "Y" else y > x
    elif sign == ">":
        return y > x if answer == "Y" else y <= x
    elif sign == "<":
        return y < x if answer == "Y" else y >= x

def find_possible_y(questions):
    for y in range(-2*10**9, 2*10**9 + 1):
        valid = True
        for sign, x, answer in questions:
            if not check_relation(x, sign, answer, y):
                valid = False
                break
        if valid:
            return y
    return "Impossible"

if __name__ == "__main__":
    n = int(input())
    questions = [input().split() for _ in range(n)]
    questions = [(sign, int(x), answer) for sign, x, answer in questions]
    
    result = find_possible_y(questions)
    print(result)
