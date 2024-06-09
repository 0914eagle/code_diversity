
def count_good_pairs(teacher_interest, student_interest):
    n = len(teacher_interest)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if teacher_interest[i] + teacher_interest[j] > student_interest[i] + student_interest[j]:
                count += 1
    return count

def main():
    n = int(input())
    teacher_interest = list(map(int, input().split()))
    student_interest = list(map(int, input().split()))
    print(count_good_pairs(teacher_interest, student_interest))

if __name__ == '__main__':
    main()

