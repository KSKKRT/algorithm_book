from bisect import bisect_left


def solution7_1():
    N = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    i = 0
    for j in range(N):
        if a[i] < b[j]: i += 1
    return i

def solution7_2():
    N = int(input())
    a = [0 for _ in range(N)]
    b = a[::]
    c = a[::]
    d = a[::]
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    for i in range(N):
        c[i], d[i] = map(int, input().split())
    frendly = 0
    return 

def solution7_3() -> str:
    """ABC131 D"""
    N = int(input())
    tasks = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
    current_time = 0
    for i in range(N):
        current_time += tasks[i][0]
        if current_time > tasks[i][1]:
            return "No"
    return "Yes"




    

if __name__ == "__main__":
    # print(solution7_1())
    # print(solution7_3())
    # solution7_3_2()