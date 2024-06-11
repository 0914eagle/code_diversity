def sort_array(arr):
    
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
/python/6kyu/count_the_smiley_faces.py


import re

