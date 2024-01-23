from collections import deque
from typing import Any


def graph_search(G: list[list[int]], s: int) -> list[list[int]]:
    """
    グラフ探索の実装(code13.1)
    繰り返し処理内のtodoをpopleftでqueueとして用いればBFS,
    popでstackとして用いればDFS
    """
    N: int = len(G)
    seen: list[bool] = [False for _ in range(N)]
    todo: deque[int] = deque()
    seen[s] = True
    todo.append(s)
    
    while len(todo) != 0:
        v = todo.popleft()
        for x in G[v]:
            if seen[x]: continue
            seen[x] = True
            todo.append(x)
    return G


class DFS:
    """
    再帰関数によるDFSの実装(code13.2)
    """
    def __init__(self, G):
        self.G = G
        self.seen = [False for _ in range(len(G))]
        self.color = [-1 for _ in range(len(G))]

    def dfs(self, v: int) -> None:
        self.seen[v] = True
        for next_v in self.G[v]:
            if self.seen[next_v]: 
                continue
            self.dfs(next_v)
        return
    
    def reset_access(self) -> None:
        self.seen = [False for _ in range(len(self.G))]
        return
    
    def dfs_bipartite(self, s, cur=0) -> bool:
        self.color[s] = cur
        for v in self.G[s]:
            if self.color[v] != -1:
                if self.color[v] == cur: return False
                continue
            if not self.dfs_bipartite(v, 1-cur): return False
        return True
    
def test13_2() -> None:
    G = [[5], [6], [3, 6], [5, 7], [1, 2, 6], [], [7], [0]]
    d = DFS(G)
    for v in range(len(G)):
        if d.seen[v]: continue
        d.dfs(v)

class BFS:
    def __init__(self, G):
        self.G = G

    def bfs(self, s: int):
        dist = [-1 for _ in range(len(self.G))]
        que: deque[int] = deque()
        dist[s] = 0
        que.append(s)
        while len(que) != 0:
            v = que.popleft()
            for x in self.G[v]:
                if dist[x] != -1: continue
                dist[x] = dist[v] + 1
                que.append(x)
        return dist

def test13_3() -> None:
    G = [[1, 2, 4], [0, 3, 4, 8], [0, 5], [1, 7, 8], [0, 1, 8], [2, 6, 8], [5, 7], [3, 6], [1, 3, 4, 5]]
    b = BFS(G)
    dist = b.bfs(0)
    print("頂点0から各頂点までの最短距離")
    for v in range(len(G)):
        print(f"頂点{v}: {dist[v]}")
    return

def test13_4() -> None:
    #各頂点にから各頂点へのパスが存在するかどうか
    G = [[1, 2, 3], [4, 7], [4], [2, 5], [6], [4, 6], [7], []]
    d = DFS(G)
    for v in range(len(G)):
        print(f"頂点{v}からのパスが存在する頂点: ", end='')
        d.dfs(v)
        canReach = [i for i in range(len(G)) if d.seen[i] and i!=v]
        print(*canReach, sep=',')
        d.reset_access()
    return

def test13_5() -> None:
    G = [[1, 3], [0, 2, 4], [1], [0, 4], [1, 3]]
    d = DFS(G)
    for v in range(len(G)):
        if d.color[v] != -1: continue
        if not d.dfs_bipartite(v): 
            print("二部グラフではありません")
            return
    print("二部グラフです")
    return

def test13_5_2() -> None:
    G2 = [[1], [0]]
    d = DFS(G2)
    for v in range(len(G2)):
        if d.color[v] != -1: continue
        if not d.dfs_bipartite(v): 
            print("二部グラフではありません")
            return
    print("二部グラフです")
    return

class TopologicalSort:
    def __init__(self, G):
        self.G = G
        self.seen = [False for _ in range(len(G))]
        self.order = []

    def rec(self, v):
        self.seen[v] = True
        for next_v in self.G[v]:
            if self.seen[next_v]: continue
            self.rec(next_v)
        self.order.append(v)

def test13_6() -> None:
    G = [[5], [3, 6], [5, 7],[0, 7], [1, 2, 6], [], [7], [0]]
    topol = TopologicalSort(G)
    for v in range(len(G)):
        if topol.seen[v]: continue
        topol.rec(v)
    topol.order = topol.order[::-1]
    for i in range(len(topol.order)-1):
        print(f"{topol.order[i]} -> ", end='')
    print(topol.order[-1])
    return

class TreeDFS:
    def __init__(self, G) -> None:
        self.G = G
        self.depth = [0 for _ in range(len(G))]
        self.subtree_size = [0 for _ in range(len(G))]

    def dfs(self, v, p=-1, d=0) -> None:
        self.depth[v] = d
        for c in self.G[v]:
            if c == p: continue
            self.dfs(c, v, d+1)

        self.subtree_size[v] = 1
        for c in self.G[v]: 
            if c == p:continue
            self.subtree_size[v] += self.subtree_size[c]
        return
    
def test13_7() -> None:
    """
    15
    0 1
    1 2
    1 3
    0 4
    4 5
    4 8
    5 6
    5 7
    8 9
    8 10
    0 11
    11 12
    11 13
    13 14
    """
    N = int(input())
    G: list[list[object]] = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    td = TreeDFS(G)
    root = 0
    td.dfs(root)
    for v in range(N):
        print(f"{v}: depth = {td.depth[v]}, subtree_size = {td.subtree_size[v]}")



def main() -> None:
    # test13_2()
    # test13_3()
    # test13_4()
    # test13_5()
    # test13_5_2()
    # test13_6()
    test13_7()
    return

if __name__ == "__main__":
    main()
        


