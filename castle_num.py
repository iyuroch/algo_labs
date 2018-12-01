import itertools

def solution(A):
    A = [k for k, g in itertools.groupby(A)]
    # left-most terrain will always contain castle
    # right-most terrain will always contain castle
    castle_num = 1
    left_castle_el = 0
    right_castle_el = len(A) - 1
    for i in range(len(A)):
        # this will cut all terrain of left border castle
        if A[i] == A[left_castle_el]:
            left_castle_el = i
        else:
            break
        
    if left_castle_el == len(A) - 1:
        return castle_num
    # now we check for the idx of right border castle
    for i in range(len(A) - 1, 0, -1):
        if A[i] == A[right_castle_el]:
            right_castle_el = i
        else:
            break
    castle_num += 1
    
    for el in range(left_castle_el + 1, right_castle_el):
        if A[el] - A[el - 1] < 0 and A[el] - A[el + 1] < 0:
            castle_num += 1
        if A[el] - A[el - 1] > 0 and A[el] - A[el + 1] > 0:
            castle_num += 1
        
    
    return castle_num