# def value(N, K, S):
#     r1 = K + N
#     r2 = K + (K - S) + (N - S)
#
#     if r1 < r2:
#         return r1
#     else:
#         return r2
#
#
# n = int(input())
# print('Case #1:', value(10, 7, 6))
# # for i in range(1, n + 1):
# #     N, K, S = list(map(int, input().split(' ')))
# #
# #     print('Case #', i,':', value(10, 5, 2))

def boringNumber(n):

    n1 = str(n)
    n1 = n1[len(n1)::-1]
    print('sadfsdf', n1)

    return 1



n = int(input())

for _ in range(n):

    L, R = list(map(int, input().split(' ')))
    sum = 0
    for i in range(L, R + 1):
        sum += boringNumber(i)

    print(f'Case #{_}: ', sum)
