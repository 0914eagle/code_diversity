
def count_good_pairs(num_topics, teacher_interest, student_interest):
    count = 0
    for i in range(num_topics):
        for j in range(i+1, num_topics):
            if teacher_interest[i] + teacher_interest[j] > student_interest[i] + student_interest[j]:
                count += 1
    return count

