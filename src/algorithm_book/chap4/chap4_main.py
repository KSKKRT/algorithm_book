def code4_4(m: int, n: int) -> int:
    """
    return gcd(m, n)
    """
    if n == 0: return m
    return code4_4(n, m%n)

def code4_6(N: int) -> int:
    """
    return fibonacci(N)
    """
    if N == 0: return 0
    elif N == 1: return 1
    return code4_6(N-1) + code4_6(N-2)

def code4_7(N: int) -> int:
    """
    フィボナッチ数列を漸化式的に線形時間で求める
    """
    F = [0 for _ in range(N)]
    F[1] = 1
    for i in range(2, N):
        F[i] = F[i-1] + F[i-2]
    return F.pop()

def memorize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memorize
def code4_8(N: int) -> int:
    """
    フィボナッチ数列を再帰で求める際に同じ計算を繰り返しているので非効率
    メモ化をすることで計算履歴を残す
    """
    if N == 0: return 0
    elif N == 1: return 1
    else:
        return code4_8(N-1) + code4_8(N-2)

def code4_9() -> str:
    """
    input: W(int), A(list)
    output: Yes if set in A st.sum(set) == W else No
    """
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    def func(i, w, A):
        if i==0:
            if w == 0: return True
            else: return False
        if func(i-1, w, A): return True
        if func(i-1, w-A[i-1], A): return True
        return False
    return "Yes" if func(N, W, A) else "No"


    


if __name__ == "__main__":
    # print(code4_4(51, 15))
    # print(code4_6(6))
    # print(code4_7(50))
    print(code4_8(7))
    # print(code4_9())
