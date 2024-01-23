class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [-1 for _ in range(n)]
        self.siz = [1 for _ in range(n)]

    def root(self, x: int) -> int:
        if self.par[x] == -1: return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
        
    def issame(self, x: int, y:int) -> bool:
        return self.root(x) == self.root(y)
    
    def size(self, x):
        return self.siz[self.root(x)]
    
    def unite(self, x: int, y:int) -> None:
        x, y = self.root(x), self.root(y)
        if x == y: return
        if self.size(x) > self.size(y):
            self.par[y] = x
            self.siz[x] += self.siz[y]
            return
        if self.size(x) <= self.size(y):
            self.par[x] = y
            self.siz[y] += self.siz[x]
            return
    
def code11_3() -> None:
    uf = UnionFind(7)
    uf.unite(1, 2)
    uf.unite(2, 3)
    uf.unite(5, 6)
    print("Both 1 and 3 are same group." if uf.issame(1, 3) else "They are in different groups.")
    print("Both 2 adn 5 are same group." if uf.issame(2, 5) else "They are in different groups.")
    uf.unite(1, 6)
    print("Both 2 adn 5 are same group." if uf.issame(2, 5) else "They are in different groups.")
    return

def code11_4() -> None:
    "連結成分の個数を求めるコード"
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for i in range(M):
        a, b = map(int, input().split())
        uf.unite(a, b)
    res = set()
    for x in range(N):
        res.add(uf.root(x))
    print(len(res))
    return

if __name__ == "__main__":
    # code11_3()
    code11_4()
