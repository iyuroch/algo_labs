
def merge(arr, left_idx, middle_idx, right_idx):
    tmp_left = arr[left_idx:middle_idx]
    tmp_right = arr[(middle_idx + 1):right_idx]
    pos_left = 0
    pos_right = 0
    while pos_left < middle_idx - left_idx and pos_right < right_idx - middle_idx

def mergesort(arr, left_idx, right_idx):
    if (left_idx < right_idx):
        middle_idx = (left_idx + right_idx) / 2
        mergesort(arr, left_idx, middle_idx)
        mergesort(arr, middle_idx + 1, right_idx)
        merge(arr, left_idx, middle_idx, right_idx)
    # return arr

if __name__ == "__main__":
    arr = [1,2,5,7,8,2,32,7,3]
    arr_len = len(arr)
    mergesort(arr, 0, arr_len - 1)
    print(arr)