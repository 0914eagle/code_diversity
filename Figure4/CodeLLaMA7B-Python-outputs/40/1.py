def triples_sum_to_zero(l: list):
    
    # Your code here
    # for i in range(len(l)):
    #     for j in range(i + 1, len(l)):
    #         for k in range(j + 1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 return True
    # return False
    #
    # # or
    #
    # for i in range(len(l)):
    #     for j in range(i + 1, len(l)):
    #         for k in range(j + 1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 return True
    # return False
    #
    # # or
    #
    # for i in range(len(l)):
    #     for j in range(i + 1, len(l)):
    #         for k in range(j + 1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 return True
    # return False

    # or

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False


print(triples_sum_to_zero([1, 3, -2, 1]))
