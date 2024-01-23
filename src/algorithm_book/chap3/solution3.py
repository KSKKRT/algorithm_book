def solution3_2() -> int:
    """
    input A: List[int], v(int)
    output the number of v in A
    test_case v:2, A:[2, 3, 4, 2, 2] -> 3
    """
    v = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(len(A)):
        if A[i] == v: count += 1
    return count

def solution3_3() -> int:
    """
    input A: List[int]
    output the second smallest number
    """
    A = list(map(int, input().split()))
    if len(A) == 2:
        return max(A)
    min_, second = A[0], A[1]
    if min_ > second: min_, second = second, min_
    for i in range(2, len(A)):
        if A[i] < min_: 
            second = min_
            min_ = A[i]
        elif A[i] < second: second = A[i]
    return second

def solution3_4() -> int:
    """
    input: A: list[int]
    output: int (Aから2つ選んだ時の差の最大値)
    最大値と最小値の差が最大になる
    """
    A = list(map(int, input().split()))
    min_value = 2000000000
    max_value = -2000000000
    for i in range(len(A)):
        if A[i] < min_value: min_value = A[i]
        if A[i] > max_value: max_value = A[i]
    return max_value - min_value

def solution3_5() -> int:
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    flag = True
    while flag:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                flag = False
                break
        count += 1
    return count-1

def solution3_5_2() -> int:
    def _exp(n:int) -> int:
        exp = 0
        while n % 2 == 0:
            n //= 2
            exp += 1
        return exp
    N = int(input())
    A = list(map(int, input().split()))
    count = 2000000000
    for i in range(N):
        count = min(count, _exp(A[i]))
    return count

    
def solution3_6() -> int:
    K, N = map(int, input().split())
    count = 0
    for i in range(K+1):
        for j in range(K+1):
           if N-K <= i + j <= N: count += 1
    return count

def solution3_7() -> int:
    S = input()
    N = len(S)
    sum_value = 0
    for bit in range(1 << N-1):
        tmp = 0
        for i in range(N-1):
            tmp *= 10
            tmp += int(S[i])
            if bit & (1<<i):
                sum_value += tmp
                tmp = 0
        else:
            tmp *= 10
            tmp += int(S[N-1])
            sum_value += tmp
    return sum_value
            


                

    

if __name__ == "__main__":
    # print(solution3_2())
    # print(solution3_3())
    # print(solution3_4())
    # print(solution3_5())
    # print(solution3_6())
    print(solution3_7())