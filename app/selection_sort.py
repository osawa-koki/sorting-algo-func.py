
def selection_sort(lst):
    # リストの要素数を取得する
    n = len(lst)
    # 各要素を順に処理する
    for i in range(n):
        min_value = lst[i]
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < min_value:
                min_value = lst[j]
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
