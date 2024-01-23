from pprint import pprint


def code5_1() -> int:
    N = int(input())
    h = list(map(int, input().split()))
    inf = 100000000
    dp = [inf for _ in range(N)]
    dp[0] = 0
    for i in range(1, N):
        if i == 1:
            dp[i] = abs(h[i]-h[i-1])
        else:
            dp[i] = min(
                dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2])
            )
    return dp[N-1]

def code5_3() -> int:
    N = int(input())
    h = list(map(int, input().split()))
    inf = 100000000
    dp = [inf for _ in range(N)]
    dp[0] = 0
    for i in range(1, N):
        if dp[i] > dp[i-1] + abs(h[i]-h[i-1]):
            dp[i] = dp[i-1] + abs(h[i]-h[i-1])
        if i > 1:
            if dp[i] > dp[i-2] + abs(h[i]-h[i-2]):
                dp[i] = dp[i-2] + abs(h[i]-h[i-2])
    return dp[N-1]

def memorize(f):
    memo = [10000000 for _ in range(100)]
    def helper(x):
        if memo[x] == 10000000:
            memo[x] = f(x)
        return memo[x]
    return helper

# @memorize
# def code5_6(N: int) -> int:
#     h = list(map(int, input().split()))
#     inf = 100000000
#     dp = [inf for _ in range(N)]
#     dp[0] = 0
#     for i in range()
#     if dp[i] < inf: return dp[i]
#     if i == 0:

class Code5_7:
    def __init__(self, N: int, W: int, weight: list[int], value: list[int]):
        self.N = N
        self.W = W
        self.weight = weight
        self.value = value
        self.dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    def _chmax(self,idx, w, a):
        if self.dp[idx][w] < a:
            self.dp[idx][w] = a
    
    def _calc(self):
        for i in range(self.N):
            for w in range(self.W+1):
                if w - self.weight[i] >= 0:
                    self._chmax(i+1, w, self.dp[i][w-self.weight[i]]+self.value[i])

                self._chmax(i+1, w, self.dp[i][w])
        
    def get_result(self):
        self._calc()
        return self.dp[self.N][self.W]
    
class Code5_8:
    def __init__(self, S, T):
        self.S = S
        self.T = T
        self.dp = [[2000000000 for _ in range(len(S)+1)] for _ in range(len(T)+1)]
        self.dp[0][0] = 0

    def _chmin(self, i, j, com):
        if self.dp[i][j] > com:
            self.dp[i][j] = com

    def get_result(self):
        for i in range(len(self.T)+1):
            for j in range(len(self.S)+1):
                if i>0 and j>0:
                    if self.T[i-1] == self.S[j-1]:
                        self._chmin(
                            i, j, self.dp[i-1][j-1]
                        )
                    else:
                        self._chmin(
                            i, j, self.dp[i-1][j-1]+1
                        )
                if i > 0:
                    self._chmin(
                        i, j, self.dp[i-1][j]+1
                    )
                if j > 0:
                    self._chmin(
                        i, j, self.dp[i][j-1]+1
                    )

        pprint(self.dp)
        return self.dp[len(self.T)][len(self.S)]



if __name__ == "__main__":
    # print(code5_1())
    # print(code5_3())
    # code5_7 = Code5_7(6, 15, [2, 1, 3, 2, 1, 5], [3, 2, 6, 1, 3, 85])
    # print(code5_7.get_result())
    code5_8 = Code5_8("logistic", "algorithm")
    print(code5_8.get_result())

        