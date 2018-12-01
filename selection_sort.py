def pop_minimum(arr, i):
    min_el = i
    for el in range(i, len(arr)):
        if arr[el] < arr[min_el]:
            min_el = el

    return arr.pop(min_el)

def selection_sort(arr):
    # tmp_arr = []
    for i in range(len(arr)):
        arr.insert(i, pop_minimum(arr, i))
    return arr

if __name__ == "__main__":
    arr = [5,1,24,9,2,4]
    arr = selection_sort(arr)
    print(arr)