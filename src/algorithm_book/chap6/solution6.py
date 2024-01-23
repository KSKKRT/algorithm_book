import bisect


def solution6_1():
    """
    座標圧縮
    """
    N = int(input())
    a = list(map(int, input().split()))
    idx = sorted(a)
    result = [0 for _ in range(N)]
    for i in range(N):
        left, right = 0, N-1
        while right >= left:
            mid = (right + left) // 2
            if idx[mid] == a[i]:
                result[i] = mid
                break
            elif idx[mid] > a[i]: right = mid - 1
            else: left = mid + 1
    return result

def solution6_1_2():
    N = int(input())
    a = list(map(int, input().split()))
    ranking = {x:i for i, x in enumerate(sorted(list(set(a))))}
    result = [ranking[x] for x in a]
    return result

def solution6_2():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    result = 0
    for i in range(N):
        num_a = bisect.bisect_left(a=A, x=B[i])
        num_c = N - bisect.bisect_right(a=C, x=B[i])
        result += (num_a * num_c)
    return result

def solution6_3():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(N)]
    return 

def solution6_6():
    from math import pi, sin
    A, B, C = map(int, input().split())
    left, right = 1, 101
    def f(A, B, C, t):
       return A*t + B*sin(C*t*pi)
    mid = 51
    while abs(f(A, B, C, mid) - 100) > 10e-6:
        mid = (right+left) / 2
        if f(A, B, C, mid) - 100 == 0: return mid
        elif f(A, B, C, mid) > 100: right = mid
        else: left = mid
    return 
        






        
if __name__ == "__main__":
    # print(solution6_1())
    # print(solution6_2())
    # print(solution6_3())
    print(solution6_6())