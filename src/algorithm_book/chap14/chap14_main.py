import heapq
from typing import Any


class Edge:
    def __init__(self, to: int, w: int):
        self.to = to
        self.w = w

class BellmanFord:
    def __init__(self) -> None:
        self.load_graph()
        self.inf = 1 << 60
        self.dist: list[int] = [self.inf for _ in range(self.N)]

    def load_graph(self) -> None:
        N, M = map(int, input().split())
        G: list[list[Any]] = [[] for _ in range(N)]
        for _ in range(M):
            a, b, w = map(int, input().split())
            G[a].append(Edge(b, w))
        self.G = G
        self.N = N
        return
    
    def chmin(self, i, j, b) -> bool:
        if self.dist[i] > self.dist[j] + b:
            self.dist[i] = self.dist[j] + b
            return True
        return False
        
    def solve(self, s: int) -> None:
        exist_negative_cycle: bool = False
        self.dist[s] = 0
        for iter in range(self.N):
            update: bool = False
            for v in range(self.N):
                if self.dist[v] == self.inf: continue
                for e in self.G[v]:
                    if self.chmin(e.to, v, e.w):
                        update = True
            if not update: break
            if iter == self.N - 1 and update: exist_negative_cycle = True
        if exist_negative_cycle: 
            print("NEGATIVE CYCLE")
            return
        else:
            for v in range(self.N):
                if s == v: continue
                print(f"頂点{v}までの最小コストは ", end="")
                if self.dist[v] < self.inf: print(self.dist[v])
                else: print("INF")
        return
    
    def reset_dist(self) -> None:
        del self.dist
        self.dist = [self.inf for _ in range(self.N)]
        return

def test14_2() -> None:
    """
    6 12
    0 1 3
    0 3 100
    1 3 57
    3 1 -5
    1 2 50
    1 4 -4
    2 3 -10
    2 4 -5
    2 5 100
    4 3 25
    4 5 8
    4 2 57
    """
    bellman_ford = BellmanFord()
    for i in range(bellman_ford.N):
        print(f"頂点{i}からの最小コスト:")
        bellman_ford.solve(s=i)
        bellman_ford.reset_dist()
    return

class Dijkstra:
    INF = 1 << 60
    
    def __init__(self) -> None:
        self._load_graph()
        self.used = [False for _ in range(self.N)]
        self.dist = [self.INF for _ in range(self.N)]

    def _chmin(self, i, j, b) -> bool:
        if self.dist[i] > self.dist[j] + b:
            self.dist[i] = self.dist[j] + b
            return True
        else:
            return False

    def _load_graph(self) -> None:
        N, M = map(int, input().split())
        G: list[list[Any]] = [[] for _ in range(N)]
        for _ in range(M):
            a, b, w = map(int, input().split())
            G[a].append(Edge(b, w))
        self.G = G
        self.N = N
        return
    
    def reset_log(self) -> None:
        self.used = [False for _ in range(self.N)]
        self.dist = [self.INF for _ in range(self.N)]
        return
    
    def solve(self, s: int) -> None:
        self.dist[s] = 0
        for _ in range(self.N):
            target_v = -1
            min_dist = self.INF
            for v in range(self.N):
                if not self.used[v] and self.dist[v] < min_dist:
                    min_dist = self.dist[v]
                    target_v = v
            if target_v == -1: break
            for e in self.G[target_v]:
                self._chmin(e.to, target_v, e.w)
            self.used[target_v] = True
        
        for v in range(self.N):
            if s == v: continue
            print(f"頂点{v}までの最短距離は", end="")
            if self.dist[v] < self.INF: print(self.dist[v])
            else: print("INF")
        return

def test14_3() -> None:
    """
    input_data:
    6 9
    0 1 3
    0 2 5
    1 2 4
    1 3 12
    2 3 9
    2 4 4
    3 5 2
    4 3 7
    4 5 8
    """
    dijk = Dijkstra()
    for i in range(dijk.N):
        print(f"頂点{i}からの最短距離:")
        dijk.solve(i)
        dijk.reset_log()
    return

class DijkstraHeap:
    INF = 1 << 60
    def __init__(self) -> None:
        self._load_graph()
        self.dist = [self.INF for _ in range(self.N)]

    def _load_graph(self) -> None:
        N, M = map(int, input().split())
        G: list[list[Any]] = [[] for _ in range(N)]
        for _ in range(M):
            a, b, w = map(int, input().split())
            G[a].append(Edge(b, w))
        self.N = N
        self.G = G
        return
    
    def _chmin(self, i, j, b) -> bool:
        if self.dist[i] > self.dist[j] + b:
            self.dist[i] = self.dist[j] + b
            return True
        return False
    
    def reset_dist(self) -> None:
        self.dist = [self.INF for _ in range(self.N)]
        return
    
    def dijkstra(self, s: int) -> None:
        self.dist[s] = 0
        que: list[tuple[int, int]] = []
        heapq.heapify(que)
        heapq.heappush(que, (self.dist[s], s))
        while len(que) != 0:
            d, v = heapq.heappop(que)
            if d > self.dist[v]: continue

            for e in self.G[v]:
                if self._chmin(e.to, v, e.w):
                    heapq.heappush(que, (self.dist[e.to], e.to))
        for v in range(self.N):
            if s == v: continue
            print(f"頂点{v}までの最短距離: ", end='')
            if self.dist[v] < self.INF: print(self.dist[v])
            else: print("INF")
        return

def test14_4() -> None:
    """
    input_data
    -------------------
    6 9
    0 1 3
    0 2 5
    1 2 4
    1 3 12
    2 3 9
    2 4 4
    3 5 2
    4 3 7
    4 5 8
    -------------------
    """
    dijk = DijkstraHeap()
    print("-------------------------")
    for v in range(dijk.N):
        print(f"頂点{v}からの最短距離: ")
        dijk.dijkstra(v)
        dijk.reset_dist()
        print("-------------------------")
    return
        
def floyd_warshall() -> None:
    """
    code14.5
    input_data
    -------------------
    6 9
    0 1 3
    0 2 5
    1 2 4
    1 3 12
    2 3 9
    2 4 4
    3 5 2
    4 3 7
    4 5 8
    -------------------
    """
    INF = 1 << 60
    N, M = map(int, input().split())
    dp = [[INF for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        dp[a][b] = w
    for v in range(N): dp[v][v] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
    exist_negative_cycle = False
    for v in range(N):
        if dp[v][v] < 0: 
            exist_negative_cycle = True
            break
    
    if exist_negative_cycle:
        print("NEGATIVE CYCLE")
        return
    else:
        for s in range(N):
            print("-----------------------")
            print(f"頂点{s}からの最短距離: ")
            for e in range(N):
                if s == e: continue
                if dp[s][e] < INF/2: print(f"頂点{e}までの最短距離: {dp[s][e]}")
                else: print(f"頂点{e}への有向パスは存在しない")
    return


    


if __name__ == "__main__":
    # test14_2()
    # test14_3()
    # test14_4()
    floyd_warshall()
