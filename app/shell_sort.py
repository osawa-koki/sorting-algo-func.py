
def shell_sort(array):
    # シェルソート用の間隔を計算
    gap = len(array) // 2
    # 間隔を半減しながら、挿入ソートを実行
    while gap > 0:
        for i in range(gap, len(array)):
            tmp = array[i]
            j = i
            while j >= gap and array[j - gap] > tmp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = tmp
        gap //= 2
    return array
