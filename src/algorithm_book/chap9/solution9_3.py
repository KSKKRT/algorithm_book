"""
(()(())())((())())のような(と)からなる長さ2Nの文字列が与えられた時，
この文字列において，括弧列が整合しているかどうかを判定し，さらに何文字目となん文字目が対応しているかをN組み求める処理を
O(N)で設計．
"""
s = input()
st = []
flag = True
result = []
for i in range(len(s)):
    if s[i] == "(":
        st.append(i)
    else:
        if len(st) == 0:
            flag = False
            break
        result.append((st.pop(), i))
if not flag:
    print("不整合")
else:
    print(*result, sep=", ")
