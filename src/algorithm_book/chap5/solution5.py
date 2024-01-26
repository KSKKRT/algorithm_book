from pprint import pprint


def solution5_1():
    N = int(input())
    happy = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(3)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                if dp[i][j] < dp[i - 1][k] + happy[i - 1][j]:
                    dp[i][j] = dp[i - 1][k] + happy[i - 1][j]
    return max(dp[N])


def solution5_2() -> str:
    N = int(input())
    W = int(input())
    A = list(map(int, input().split()))
    dp = [[False for _ in range(W + 1)] for i in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(W + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j >= A[i] and dp[i][j - A[i]]:
                dp[i + 1][j] = True
    return "Yes" if dp[N][W] else "No"


def solution5_3() -> int:
    N = int(input())
    A = list(map(int, input().split()))
    W = sum(A)
    dp = [[False for _ in range(W + 1)] for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(W + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j >= A[i] and dp[i][j - A[i]]:
                dp[i + 1][j] = True
    return sum(dp[N])


def solution5_4() -> None:
    N = int(input())
    a = list(map(int, input().split()))
    W = int(input())
    K = int(input())
    dp = [[1 << 60 for _ in range(W + 1)] for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(W + 1):
            if dp[i][j] < dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j]
            if j >= a[i] and dp[i + 1][j] > dp[i][j - a[i]] + 1:
                dp[i + 1][j] = dp[i + 1][j] + 1
    print(dp)
    print('Yes' if dp[N][W] <= K else 'No')
    return


def solution5_5() -> None:
    N = int(input())
    a = list(map(int, input().split()))
    W = int(input())


def solution5_7() -> str:
    S = input()
    T = input()
    dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
    inv_result = ''
    i, j = len(S), len(T)
    while i > 0 and j > 0:
        if dp[i - 1][j - 1] == dp[i - 1][j] == dp[i][j - 1] == dp[i][j] - 1:
            inv_result += S[i - 1]
            i -= 1
            j -= 1
            continue
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return inv_result[::-1]


if __name__ == "__main__":
    # print(solution5_1())
    # print(solution5_2())
    # print(solution5_3())
    solution5_4()
    # print(solution5_7())
