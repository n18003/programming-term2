#コンビニの支払いの金額を求める
#値段
bear_v = 200
otumami_v = 100
yakitori_v = 100
#個数
bear_c = 2
otumami_c = 1
yakitori_c = 2
#割引
rate = 0.8
point_kard = 150

#計算
sum_v = (bear_v * bear_c) + (otumami_v * otumami_c) + (yakitori_v * yakitori_c)
payment = ((bear_v * bear_c) + (otumami_v * otumami_c) + ((yakitori_v * rate) * yakitori_c)) - (point_kard)

#結果を表示
print("買い物の合計は", sum_v,"円")
print("割引等してもらうと", payment, "円")
