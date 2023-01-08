
def bubble_sort(lst):
    # リストの長さを取得
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            # リスト内の要素を比較し、順序が逆の場合は交換する
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
