
def sleep_sort(array):
    def merge(array):
        result = []
        for element in array:
            result.extend(element)
        return result
    # スリープを用意する
    sleep = [[] for _ in range(max(array) + 1)]
    # スリープに要素を詰める
    for x in array:
        sleep[x].append(x)
    return merge(sleep)
