def sort_array(array):
    
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        if (array[0] + array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)
/python/easy/100_199/150_159/157_reverse_words_in_a_string_iii.py



class