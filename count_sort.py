def count_sort(arr):
    occurence_map = dict()
    for el in arr:
        try:
            occurence_map[el] += 1
        except KeyError:
            occurence_map[el] = 1
    curr_idx = 0
    for key in sorted(occurence_map.keys()):
        for _ in range(occurence_map[key]):
            arr[curr_idx] = key
            curr_idx += 1
    return arr

if __name__ == "__main__":
    arr = [1,2,2,3,1,3,2,5,2,3,5]
    print(count_sort(arr))