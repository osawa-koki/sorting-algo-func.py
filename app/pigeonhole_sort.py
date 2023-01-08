
def pigeonhole_sort(array):
    # 最大値と最小値を見つける
    min_val = min(array)
    max_val = max(array)
    # 鳩の巣のリストを用意する
    pigeonhole_array = [0] * (max_val - min_val + 1)
    # 鳩の巣に要素を詰める
    for x in array:
        pigeonhole_array[x - min_val] += 1
    # 鳩の巣から要素を取り出す
    i = 0
    for count in pigeonhole_array:
        for j in range(count):
            array[i] = min_val
            i += 1
        min_val += 1
    return array
