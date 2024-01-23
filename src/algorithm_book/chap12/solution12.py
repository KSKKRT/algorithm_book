from bisect import bisect_left


def solution12_1() -> None:
    A = list(map(int, input().split()))
    rank = [0 for _ in range(len(A))]
    sorted_A = sorted(A)
    for i in range(len(A)):
        rank[i] = bisect_left(sorted_A, A[i])
    print(A, "\n", rank)
    return

def solution12_2() -> None:
    N, M = map(int, input().split())
    stores = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    cur, res, i = 0, 0, 0
    while True:
        if cur + stores[i][1] < M:
            res += stores[i][0] * stores[i][1]
            cur += stores[i][1]
        else:
            res += stores[i][0] * (M - cur)
            break
        i += 1
    print(res)
        


if __name__ == "__main__":
    # solution12_1()
    solution12_2()