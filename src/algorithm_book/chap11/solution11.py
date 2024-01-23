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

def solution11_1() -> None:
    """ABC075 C"""
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append([a-1, b-1])

    def countLinkedComponents(uf: UnionFind) -> int:
        res = 0
        for i in range(N):
            if i == uf.root(i):
                res += 1
        return res

    res = 0
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if i == j: continue
            uf.unite(edges[j][0], edges[j][1])
        if countLinkedComponents(uf) != 1: res += 1
    print(res)
    return

def solution11_2() -> None:
    def countLinkedComponents(uf: UnionFind) -> int:
        res = 0
        roots = [i for i in range(len(uf.par)) if uf.par[i] == -1]
        vers = [uf.siz[root] for root in roots]
        for i in range(len(vers)-1):
           res += vers[i] * vers[i+1]
        return res
    
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    uf = UnionFind(N)
    res = []
    for i in range(M-1, 0, -1):
        res.append(countLinkedComponents(uf))
        a, b = edges[i][0], edges[i][1]
        uf.unite(a-1, b-1)
    for n in res[::-1]:
        print(n)
    return
        

    



if __name__ == "__main__":
    # solution11_1()
    solution11_2()