
def merge_sort(lst):
    # リストの要素数を取得する
    n = len(lst)
    # リストの要素数が1以下の場合はそのまま返す
    if n <= 1:
        return lst
    # 中央の位置を計算する
    mid = n // 2
    # リストを分割する
    left = lst[:mid]
    right = lst[mid:]
    # 分割したリストを再帰的にマージソートする
    left = merge_sort(left)
    right = merge_sort(right)
    # 分割したリストをマージする
    return merge(left, right)

def merge(left, right):
    merged = []
    # 左右のリストを比較しながらマージする
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged
