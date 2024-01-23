class UnionFind:

    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x: int) -> int:
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y) -> bool:
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.siz[rx] < self.siz[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x: int) -> int:
        return self.siz[self.root(x)]
    
class Edge:
    def __init__(self, u:int, v:int, w:int) -> None:
        self.u = u
        self.v = v
        self.w = w

class Kruskal:
    INF = 1 << 60

    def __init__(self) -> None:
        self._load()

    def _load(self) -> None:
        N, M = map(int, input().split())
        edges = []
        for _ in range(M):
            u, v, w = map(int, input().split())
            edges.append(Edge(u, v, w))
        self.edges = sorted(edges, key=lambda x: x.w)
        self.N = N
        self.M = M
        return
    
    def solve(self) -> None:
        res = 0
        res_edges = []
        uf = UnionFind(self.N)
        for i in range(self.M):
            e = self.edges[i]
            u, v, w = e.u, e.v, e.w
            if uf.issame(u, v): continue
            uf.unite(u, v)
            res += w
            res_edges.append((u, v))
        print(f"最小全域木の重み: {res}")
        print(f"最小全域木を構成する辺の集合: {res_edges}")
        return

if __name__ == "__main__":
    """
    input_data
    -----------------
    8 12
    0 3 5
    0 5 6
    0 7 3
    1 3 8
    1 4 4
    1 6 3
    2 5 10
    2 7 5
    2 4 9
    3 7 6
    4 6 2
    6 7 7
    """
    k = Kruskal()
    k.solve()
    
