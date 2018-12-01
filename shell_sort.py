import math

def insert_sort(arr):
    sorted_idx = 0

    for _ in range(len(arr)):
        sorted_el = sorted_idx
        if sorted_el == len(arr) - 1:
            break
        while arr[sorted_el] > arr[sorted_el + 1]:
            arr[sorted_el], arr[sorted_el + 1] = arr[sorted_el + 1], arr[sorted_el]
            sorted_el -= 1
            if sorted_el <= 0:
                break
        sorted_idx += 1

    return arr

def shell_sort(arr):
    arr_len = len(arr)
    gap = arr_len / 2

    while gap > 0:
        for i in range(arr_len - gap):
            if arr[i] > arr[gap + i]:
                arr[i], arr[gap + i] = arr[gap + i], arr[i]
        gap /= 2

    arr = insert_sort(arr)

    return arr

if __name__ == "__main__":
    arr = [6,2,5,7,9,1,3]
    arr = shell_sort(arr)
    print(arr)

    arr = [12,4,6,7,2,2,8]
    arr = shell_sort(arr)
    print(arr)