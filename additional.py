from count_sort import count_sort
from boyer_moore_sbstring import boyers_moore


if __name__ == "__main__":
    arr = ['a', 'b', 1, 'c', 5, 1, 5, 2, 3, -1, 8, 9, 'l']
    arr = list(map(lambda x: x + 10, filter(lambda x: isinstance(x, int) and x >= 0, arr)))
    print(count_sort(arr))

    txt = "here look now you don't know this here"
    pattern = "here"
    try:
        last_occurence = list(boyers_moore(txt, pattern))[-1]
        print(txt[:last_occurence])
    except IndexError:
        print("Can't find your pattern")
        