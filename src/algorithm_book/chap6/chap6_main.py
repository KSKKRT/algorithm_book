def code6_1():
    """
    二分探索法
    input: key
    const: N=8, a = [3, 5, 8. 10, 14, 17, 21, 39]
    output: loc of key in a (if false return -1)
    """
    key = int(input("検索したい整数値を入力してください -> "))
    N = 8
    a = [3, 5, 8, 10, 14, 17, 21, 39]
    left, right = 0, N - 1
    while right >= left:
        mid = left + (right - left) // 2
        if a[mid] == key: return mid
        elif a[mid] > key: right = mid - 1
        elif a[mid] < key: left = mid + 1
    return -1

def code6_3() -> None:
    """"
    年齢当てゲーム
    二分探索方を適用
    事前情報は80歳以下という情報のみ
    2**6 = 64 < 80 < 128 = 2**7より7回聞ければ当てれるはず
    """
    print("【GAME START】")
    left = 0
    right = 80
    while right - left > 1:
        mid = left + (right - left) // 2
        ans = input(f"{mid}歳以下ですか? (yes / no)\n")
        if ans == "yes": right = mid
        else: left = mid
    print(f"貴方は{mid}歳です！！")

def code6_4():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    min_value = 2000000000
    for i in range(N):
        left = 0
        right = N-1
        while right - left > 1:
            mid = left + (right - left) // 2
            if b[mid] == K - a[i]:
                min_value = K
                break
            elif b[mid] > K - a[i]: right = mid
            else: left = mid
        if a[i] + b[right] < min_value:
            min_value = a[i] + b[right]
    return  min_value
        
def code6_5():
    inf = 1 << 60
    N = int(input())
    H = [0 for _ in range(N)]
    S = [0 for _ in range(N)]
    for i in range(N):
        H[i], S[i] = map(int, input().split())
    left, right = 0, inf
    while right - left > 1:
        mid = (right + left) // 2
        flag = True
        time_limit = [0 for _ in range(N)]
        for i in range(N):
            if H[i] > mid: flag = False
            else: time_limit[i] = (mid - H[i]) // S[i]
        time_limit.sort()
        for i in range(N):
            if time_limit[i] < i: flag = False
        if flag: right = mid
        else: left = mid
    return right

if __name__ == "__main__":
    # print(code6_1())
    # code6_3()
    # print(code6_4())
    print(code6_5())
