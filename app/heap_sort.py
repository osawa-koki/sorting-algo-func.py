import heapq

def heap_sort(array):
    heapq.heapify(array)  # ヒープを作成
    return [heapq.heappop(array) for i in range(len(array))]  # リストを返す
