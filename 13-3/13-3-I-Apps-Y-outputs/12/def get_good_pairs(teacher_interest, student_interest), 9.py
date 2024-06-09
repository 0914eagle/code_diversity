
def get_good_pairs(teacher_interest, student_interest):
    n = len(teacher_interest)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if teacher_interest[i] + teacher_interest[j] > student_interest[i] + student_interest[j]:
                count += 1
    return count

