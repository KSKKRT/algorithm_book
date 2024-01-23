from collections import deque
from typing import Any


class Solution13_1:
    def __init__(self):
        self.G = [[1, 2, 8], [0, 2, 3], [0, 1, 5, 7], [1, 4], [3, 5], [2, 4, 6], [5, 8], [2, 8], [0, 6, 7], [], [11], [10, 12], [11]]
        self.root = [-1 for _ in range(len(self.G))]

    def _dfs(self, v):
        if self.root[v] == -1:
            self.root[v] = v
        for next_v in self.G[v]:
            if self.root[next_v] != -1: continue
            self.root[next_v] = self.root[v]
            self._dfs(next_v)
    
    def solve(self):
        for v in range(len(self.G)):
            if self.root[v] != -1: continue
            self._dfs(v)
        return len(set(self.root))
    
class Solution13_2:
    def __init__(self) -> None:
        self.G: list[list[Any]] = [[1, 2, 3], [4, 7], [4], [2, 5], [6], [4, 6], [7], []]
        self.seen: list[bool] = [False for _ in range(len(self.G))]
        self.que: deque[int] = deque()

    def bfs(self, s) -> None:
        self.seen[s] = True
        self.que.append(s)
        while len(self.que) != 0:
            v = self.que.popleft()
            for next_v in self.G[v]:
                if self.seen[next_v]: continue
                self.seen[next_v] = True
                self.que.append(next_v)
        return
    
    def solve(self) -> None:
        s = int(input("入力された頂点から他の頂点へのパスがあるか調べます -> "))
        self.bfs(s)
        for i in range(len(self.G)):
            if i == s: continue
            print(f"頂点{s}から頂点{i}へのパスは存在", end="")
            print("する" if self.seen[i] else "しない")
        return
        


        

def main() -> None:
    # s_1 = Solution13_1()
    # print(s_1.solve())
    s_2 = Solution13_2()
    s_2.solve()


if __name__ == "__main__":
    main()