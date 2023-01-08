
def bucket_sort(array, bucket_size=5):
    # 最大値と最小値を取得
    max_val = max(array)
    min_val = min(array)
    # バケットの数を計算
    bucket_count = (max_val - min_val) // bucket_size + 1
    # バケットを用意
    buckets = [[] for _ in range(bucket_count)]
    # 各要素をバケットに分類
    for a in array:
        buckets[(a - min_val) // bucket_size].append(a)
    # 各バケット内を昇順に並べ替え
    buckets = [sorted(bucket) for bucket in buckets]
    # 結果を格納するリストを用意
    result = []
    # バケットを結合
    for bucket in buckets:
        result.extend(bucket)
    return result
