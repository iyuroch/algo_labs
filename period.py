def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range( l // 2, 1, -1):
        ok = True
        for i in range(l - 2 * p, l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1

# def solution(n):
#     d = [0] * 30
#     l = 0
#     while (n > 0):
#         d[l] = n % 2
#         n //= 2
#         l += 1
#     for p in range(1, 1 + l):
#         ok = True
#         for i in range(l - p):
#             if d[i] != d[i + p]:
#                 ok = False
#                 break
#         if ok:
#             return p
#     return -1

x = 955
print(solution(x))