#最弱ジャンケンプログラム
hand = input("何を出しますか？1:グー、2:チョキ、3:パー")
if hand == str(1):
   result = "あなたはグー、CPUはパーを出しました。あなたの負けです。"
elif hand == str(2):
    result = "あなたはチョキ、CPUはグーを出しました。あなたの負けです。"
elif hand == str(3):
    result = "あなたはパー、CPUはチョキを出しました。あなたの負けです。"
else:
    result = "入力に失敗しました。もう一度最初からお願いします。"
print (result)



