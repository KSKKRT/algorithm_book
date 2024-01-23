def code7_1():
    coins = [500, 100, 50, 10, 5, 1]
    X = int(input())
    a = [2, 1, 5, 100, 50, 100]
    result = 0
    for i in range(6):
        add = X // coins[i]
        if add > a[i]: add = a[i]
        X -= coins[i] * add
        result += add
    return result

def code7_2():
    N = int(input())
    intervals = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[1])
    res = 0
    current_end_time = 0
    for i in range(N):
        if intervals[i][0] < current_end_time: continue
        res += 1
        current_end_time = intervals[i][1]
    return res


def code7_3():
    N = int(input())
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    sum = 0
    for i in range(N-1, -1, -1):
        A[i] += sum
        r = A[i] % B[i]
        if r != 0:
            sum += B[i] - r
    return sum

if __name__ == "__main__":
    # print(code7_1())
    # print(code7_2())
    print(code7_3())
