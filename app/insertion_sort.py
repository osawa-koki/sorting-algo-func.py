
def insertion_sort(lst):
    # リストの要素数を取得する
    n = len(lst)
    for i in range(1, n):
        value = lst[i]
        j = i
        while j > 0 and lst[j - 1] > value:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = value
    return lst
