
def search_el(arr, left_idx, right_idx, el):
    middle_idx = (left_idx + right_idx) / 2
    if arr[middle_idx] == el:
        return middle_idx
    if left_idx == right_idx:
        return False
    elif arr[middle_idx] < el:
        return search_el(arr, middle_idx + 1, right_idx, el)
    elif arr[middle_idx] > el:
        return search_el(arr, left_idx, middle_idx - 1, el)


def binary_search(arr, el):
    left_idx = 0
    right_idx = len(arr) - 1
    idx = search_el(arr, left_idx, right_idx, el)
    return idx

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    el = 7 #idx = 6
    el = 2
    el = 0
    el = 9
    el = 8
    el = 1
    idx = binary_search(arr, el)
    print(idx, arr[idx])