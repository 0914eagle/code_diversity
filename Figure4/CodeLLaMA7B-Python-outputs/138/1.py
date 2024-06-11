def is_equal_to_sum_even(n):
    
    if n % 2 == 1:
        return False
    else:
        for i in range(1, n):
            if i % 2 == 1:
                continue
            else:
                for j in range(i, n):
                    if j % 2 == 1:
                        continue
                    else:
                        for k in range(j, n):
                            if k % 2 == 1:
                                continue
                            else:
                                for l in range(k, n):
                                    if l % 2 == 1:
                                        continue
                                    else:
                                        if i + j + k + l == n:
                                            return True
                                        else:
                                            continue
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
        else:
            return False


