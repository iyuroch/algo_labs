def bubble_sort(arr):
    arr_len = len(arr)
    sort = 0

    if arr_len == 1:
        return arr

    while sort != arr_len:
        for el_idx in range(arr_len - sort):
            if el_idx == arr_len - 1:
                break
            elif arr[el_idx] > arr[el_idx + 1]:
                arr[el_idx], arr[el_idx + 1] = arr[el_idx + 1], arr[el_idx]
        sort += 1
        
    return arr


if __name__ == "__main__":
    arr = [17,5,3,1,123,2,5]
    arr = bubble_sort(arr)
    print(arr)
    # print(1 > arr[7])