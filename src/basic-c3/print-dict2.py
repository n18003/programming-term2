fruits = {"バナナ": 300,
          "オレンジ": 240,
          "イチゴ": 350,
          "マンゴー": 400}

for name, price in fruits.items():
    s = "{0}は、{1}円です。".format(name,price)
    print(s)
