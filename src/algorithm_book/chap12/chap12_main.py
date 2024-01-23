from random import randint


def code12_1() -> None:
    """
    挿入ソート: in-place, 安定性
    元の配列とソート後の配列を表示
    """
    N = int(input())
    A = list(map(int, input().split()))
    print("ソート前: ", A)
    for i in range(1, N):
        v = A[i]
        j = i
        while j > 0:
            if A[j-1] > v:
                A[j] = A[j-1]
                j -= 1
            else:
                break
        A[j] = v
    print("ソート後: ", A)
    return

class MergeSort:
    def __init__(self, A):
        self.A = A

    def ms(self, left: int, right: int):
        if right - left == 1: return  #ソート範囲が1の時はそのまま返す
        mid = int((right + left)/2)
        self.ms(left=left, right=mid)
        self.ms(left=mid, right=right)
        buf = self.A[left:mid] + self.A[right-1:mid-1:-1]
        idx_left, idx_right = 0, len(buf) - 1
        for i in range(left, right):
            if buf[idx_left] <= buf[idx_right]:
                self.A[i] = buf[idx_left]
                idx_left += 1
            else:
                self.A[i] = buf[idx_right]
                idx_right -= 1
        return

class QuickSort:
    def __init__(self, A) -> None:
        self.A = A
    
    def _swap(self, idx1, idx2) -> None:
        self.A[idx1], self.A[idx2] = self.A[idx2], self.A[idx1]
    
    def qs(self, left, right) -> None:
        if right - left <= 1:
            return
        pivot_idx = (right + left) // 2
        pivot = self.A[pivot_idx]
        self._swap(right-1, pivot_idx)
        i = left
        for j in range(left, right-1):
            if self.A[j] < pivot:
                self._swap(i, j)
                i += 1
        self._swap(i, right - 1)
        self.qs(left, i)
        self.qs(i+1, right)
        return

class RandomizedQuickSort:
    def __init__(self, A) -> None:
        self.A = A
    
    def _swap(self, idx1, idx2) -> None:
        self.A[idx1], self.A[idx2] = self.A[idx2], self.A[idx1]
    
    def qs(self, left, right) -> None:
        if right - left <= 1:
            return
        pivot_idx = randint(left, right-1)
        pivot = self.A[pivot_idx]
        self._swap(right-1, pivot_idx)
        i = left
        for j in range(left, right-1):
            if self.A[j] < pivot:
                self._swap(i, j)
                i += 1
        self._swap(i, right - 1)
        self.qs(left, i)
        self.qs(i+1, right)
        return

class HeapSort:
    def __init__(self, A) -> None:
        self.A = A
    
    def _swap(self, idx1, idx2) -> None:
        self.A[idx1], self.A[idx2] = self.A[idx2], self.A[idx1]

    def _Heapify(self, i: int, N: int) -> None:
        child1 = i * 2 + 1
        if child1 >= N: return
        if child1 + 1 < N and self.A[child1] < self.A[child1 + 1]: child1 += 1
        if self.A[child1] <= self.A[i]: return
        self._swap(i, child1)
        self._Heapify(child1, N)

    def heapsort(self) -> None:
        N = len(self.A)
        for i in range(int(N/2 - 1), -1, -1):
            self._Heapify(i, N)
        for i in range(N-1, -1, -1):
            self._swap(0, i)
            self._Heapify(0, i)
        return


def code12_2() -> None:
    A = [12, 9, 5, 3, 8, 17, 6, 1]
    print("ソート前: ", A)
    ms = MergeSort(A[::])
    ms.ms(left=0, right=len(A))
    print("ソート後: ", ms.A)
    print(A)
    ms2 = MergeSort(A)
    ms2.ms(left=0, right=5)
    print(ms2.A)
    return

def code12_3() -> None:
    A = [12, 9, 5, 3, 8, 17, 6, 1]
    qs = QuickSort(A)
    qs.qs(left=0, right=len(A))
    print(qs.A)
    return

def code12_4() -> None:
    A = [4, 2, 1, 8, 3, 5, 18, 13]
    print("ソート前： ", A)
    qs = RandomizedQuickSort(A)
    qs.qs(left=0, right=len(qs.A))
    print("ソート後: ", qs.A)
    return

def code12_5() -> None:
    A = [4, 2, 1, 8, 3, 5, 18, 13]
    hs = HeapSort(A)
    hs.heapsort()
    print(hs.A)
    return

class BucketSort:
    def __init__(self, A):
         self.A = A
         self.MAX = 100000
         self.sum = [0 for _ in range(self.MAX)]
         self.res = [0 for _ in range(len(self.A))]
         self._setBucket()
         self._sort()

    def _setBucket(self) -> None:
        num = [0 for _ in range(self.MAX)]
        for i in range(len(self.A)):
            num[self.A[i]] += 1
        for i in range(1, self.MAX):
            self.sum[i] = self.sum[i-1] + num[i]
        return
    
    def _sort(self) -> None:
        for i in range(len(self.A)-1, -1, -1):
            self.sum[self.A[i]] -= 1
            self.res[self.sum[self.A[i]]] = self.A[i]
        return
    
def code12_6() -> None:
    A = [5, 4, 8, 19, 3, 2, 1]
    bs = BucketSort(A)
    print(bs.res)
    return


        

    

if __name__ == "__main__":
    # code12_1()
    # code12_2()
    # code12_3()
    # code12_4()
    # code12_5()
    code12_6()