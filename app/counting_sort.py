
def counting_sort(array):
    # 最大値を取得
    max_val = max(array)
    # カウント用の配列を用意
    count = [0] * (max_val + 1)
    # 各要素の出現回数をカウント
    for a in array:
        count[a] += 1
    # 結果を格納するリストを用意
    result = []
    # カウントをもとに結果を作成
    for i, c in enumerate(count):
        result.extend([i] * c)
    return result
