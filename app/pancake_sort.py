
def pancake_sort(array):
    n = len(array)
    for i in range(n, 1, -1):
        # 最大値を見つける
        j = array.index(max(array[:i]))
        # 最大値を最後尾に移動
        if j != i - 1:
            array = array[j::-1] + array[j+1:]
            array = array[i-1::-1] + array[i:]
    return array
