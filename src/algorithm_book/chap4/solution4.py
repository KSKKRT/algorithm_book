import time


def memorize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def solution4_1(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return solution4_1(N - 1) + solution4_1(N - 2) + solution4_1(N - 3)


@memorize
def solution4_2(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return solution4_1(N - 1) + solution4_1(N - 2) + solution4_1(N - 3)


class Solution4_5:
    def __init__(self, N):
        self.N = N
        self.counter = 0

    def _func(self, cur, use):
        if cur > self.N:
            return
        if use == 0b111:
            self.counter += 1
        self._func(cur * 10 + 3, use | 0b001)
        self._func(cur * 10 + 5, use | 0b010)
        self._func(cur * 10 + 7, use | 0b100)

    def answer(self):
        self._func(0, 0b0)
        return self.counter


def memorize_2dim(f):
    memo = [[-100 for _ in range(1000)] for _ in range(1000)]

    def helper(i, w, A):
        if memo[i][w] == -100:
            memo[i][w] = f(i, w, A)
        return memo[i][w]

    return helper


@memorize_2dim
def solution4_6(N, W, A):
    """
    input: W(int), A(list)
    output: Yes if set in A st.sum(set) == W else No
    """

    def func(i, w, A):
        if i == 0:
            if w == 0:
                return True
            else:
                return False
        if func(i - 1, w, A):
            return True
        if func(i - 1, w - A[i - 1], A):
            return True
        return False

    return "Yes" if func(N, W, A) else "No"


class Tribonacchi:
    def __init__(self):
        self.memo = [0, 0, 1] + [-1 for _ in range(1000)]

    def solve(self, N: int):
        if self.memo[N] != -1:
            return self.memo[N]
        self.memo[N] = self.solve(N - 1) + self.solve(N - 2) + self.solve(N - 3)
        return self.memo[N]


if __name__ == "__main__":
    N = int(input())
    # s = time.time()
    # print(solution4_1(N))
    # e = time.time()
    # print(f"メモ化なしの再帰による算出時間(N={N}): {e-s:.8f}s")
    # print(solution4_2(9))
    # sol4_5 = Solution4_5(999999999)
    # print(sol4_5.answer())
    # print(solution4_6(4, 14, [30, 2, 63, 5]))
    tri = Tribonacchi()
    s = time.time()
    print(tri.solve(N))
    e = time.time()
    print(f"メモ化有りの場合: {e-s:.8f}s")
