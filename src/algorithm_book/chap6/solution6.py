import bisect


def solution6_1() -> None:
    N = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    res = []
    for i in range(N):
        left, right = 0, N - 1
        while right >= left:
            mid = (right + left) // 2
            if sorted_a[mid] == a[i]:
                res.append(mid)
                break
            elif sorted_a[mid] > a[i]:
                right = mid - 1
            else:
                left = mid + 1
    print(res)
    return


def solution6_1_2() -> None:
    N = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    res = [bisect.bisect_left(a=sorted_a, x=a[i]) for i in range(N)]
    print(res)
    return


def solution6_2() -> None:
    N = int(input())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    c = sorted(list(map(int, input().split())))
    res = 0
    for b_i in b:
        res += (bisect.bisect_left(a=a, x=b_i)) * (N - bisect.bisect_right(a=c, x=b_i))
    print(res)
    return


def solution6_3() -> None:
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    a_a = sorted([a[i] * a[j] for i in range(N) for j in range(N)])
    res = 0
    for i in range(len(a_a)):
        idx = bisect.bisect_right(
            a=a_a, x=M - a_a[i]
        )  # Mを超えない範囲なのでMになっても良いのでbisect_right
        if idx == 0:
            continue
        res = max(res, a_a[idx - 1] + a_a[i])
    print(res)
    return


def solution6_4() -> None:
    N, M = map(int, input().split())
    a = sorted([int(input()) for _ in range(N)])
    left, right = 0, 2 * a[-1]
    while right - left > 1:
        x = (right + left) // 2
        cnt = 1
        prev = 0
        for i in range(N):
            if a[i] - a[prev] >= x:
                cnt += 1
                prev = i
        if cnt >= M:
            left = x
        else:
            right = x
    print(left)
    return


def solution6_5() -> None:
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    left, right = 0, 10**18
    while right - left > 1:
        x = (right + left) // 2
        cnt = 0
        for i in range(N):
            target = x // a[i]
            cnt += bisect.bisect_right(a=b, x=target)
        if cnt >= K:
            right = x
        else:
            left = x
    print(right)
    return


def solution6_6() -> None:
    import math

    A, B, C = map(int, input().split())

    def f(t):
        return A * t + B * math.sin(C * t * math.pi)

    left, right = 0.0, 200.0
    for _ in range(100):
        mid = (left + right) / 2
        if f(mid) > 100:
            right = mid
        else:
            left = mid
    print(left)
    return


def solution6_7() -> None:
    import bisect

    N = int(input())
    a = sorted(list(map(int, input().split())))
    med = N * (N + 1) / 2 // 2
    left, right = 0, max(a) + 1
    while right - left > 1:
        mid = (right + left) // 2
        idx = bisect.bisect_left(a=a, x=mid)
        if idx * (idx + 1) / 2 > med:
            right = mid
        else:
            left = mid
    print(a[left])
    return


if __name__ == '__main__':
    # solution6_1()
    # solution6_1_2()
    # solution6_2()
    # solution6_3()
    # solution6_4()
    # solution6_5()
    # solution6_6()
    solution6_7()
