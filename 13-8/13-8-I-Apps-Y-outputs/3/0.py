
def get_box_holder(box_holder, questions):
    for question in questions:
        if question[1] == "T":
            box_holder = (box_holder + 1) % 8
        elif question[1] == "P":
            pass
        else:
            return box_holder
    return box_holder

def get_final_box_holder(box_holder, questions):
    for question in questions:
        if question[1] == "T":
            box_holder = (box_holder + 1) % 8
        elif question[1] == "P":
            pass
        else:
            return box_holder
    return box_holder

if __name__ == '__main__':
    box_holder = int(input())
    questions = []
    for _ in range(int(input())):
        questions.append(tuple(map(int, input().split())))
    final_box_holder = get_final_box_holder(box_holder, questions)
    print(final_box_holder)

