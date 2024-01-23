def code3_1() -> None:
    """
    線形探索法
    input: N(int),v(int),A(list[int], len(A)==N)
    print: Yes if a_i == v else No
    output: None
    test_case: N == 5, v == 7, a == [4, 3, 12, 7, 11] -> Yes
    """
    N, v = map(int, input().split())
    A = list(map(int, input().split()))
    exist = False
    for i in range(N):
        if A[i] == v: exist = True
    print("Yes" if exist else "No")

    """
    for i in range(N):
        if a[i] == v:
            print("Yes")
            break
    print("No")
    """

def code3_2() -> int:
    """
    線形探索法
    input: N(int),v(int),A(list[int], len(A)==N)
    output: i if a_i == v else -1
    test_case: N == 5, v == 7, a == [4, 3, 12, 7, 11] -> 3
    """
    N, v = map(int, input().split())
    A = list(map(int, input().split()))
    found_id = -1
    for i in range(N):
        if A[i] == v: found_id = i
    return found_id

def code3_3() -> int:
    """
    線形探索法
    input: N(int) ,A(list[int], len(A)==N)
    output: min(A)
    test_case: N == 5, a == [4, 3, 12, 7, 11] -> 3
    """
    N = int(input())
    A = list(map(int, input().split()))
    min_value = 200000000
    for i in range(N):
        if A[i] < min_value: min_value = A[i]
    return min_value

def code3_4() -> int:
    """
    線形探索法
    input: N(int), K(int), A(list[int], len(A)==N), B(list[int], len(B)==N)
    output: min(A[i]+B[j]) st. A[i] + B[j] >= K
    test_case: N == 3, K == 10, A == [8, 5, 4], B == [4, 1, 9] -> 12
    """
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    min_value = 200000000
    for i in range(N):
        for j in range(N):
            if A[i]+B[j] < K: continue
            if A[i]+B[j] < min_value: min_value = A[i]+B[j]
    return min_value

def code3_5() -> str:
    """
    部分和問題に対するビット演算を用いた全探査
    input: N(int), W(int),, A(list(int), len(A)==N)
    output: Yes if set in A st. sum(set) == W else No
    test_case: N=5,W=10,A=[1, 2, 4, 5, 11] -> Yes
    A[0]+A[2]+A[3] = 1 + 4 + 5 = 10
    """
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    for bit in range(1 << N):
        sum_ = 0
        for i in range(N):
            if bit & (1 << i): sum_ += A[i]
        if sum_ == W: return "Yes"
    
    return "No"

if __name__ == "__main__":
    # code3_1()
    # print(code3_2())
    # print(code3_3())
    # print(code3_4())
    print(code3_5())