def solution8_7():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    K = int(input())
    D = {i: False for i in range(K+1)}
    for i in range(len(a)):
        D[a[i]] = True
    for i in range(len(b)):
        if D[K-b[i]]: return True
    return False
    