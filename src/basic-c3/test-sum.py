#あるクラスの国語テストの点数をリストに代入
points = [88,76,67,43,79,80,91]

#テストの合計を求める
sum_v = 0
for _ in points:
    sum_v += _
    print(_,"点を足して合計は", sum_v)

ave_v = sum_v / len(points)
print("平均点は", ave_v, "点")
