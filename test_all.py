import math

from selection_sort import selection_sort, pop_minimum
from shell_sort import insert_sort, shell_sort
from bubble_sort import bubble_sort


if __name__ == "__main__":
    # from 2 single-dimensioned array
    # make new one, which include all even
    # number from first, and odd from second
    first_arr = [2,3,4,7,6,5,8,9]
    sec_arr = [1,3,5,2,3,4,8]
    arr = list(filter(lambda x: x % 2 == 0, first_arr)) + list(filter(lambda x: x % 2 != 0, sec_arr))
    print(insert_sort(arr))
    print(selection_sort(arr))
    print(bubble_sort(arr))