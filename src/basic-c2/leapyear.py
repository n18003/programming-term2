year = int(input("西暦何年　？"))

is_leap = False

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            is_leap = True
        else: #
            is_leap = False
    else: #
        is_leap = True
else: #
    is_leap = False

    #結果を表示
if is_leap: #
    print ("うるう年です")
else:
    print("平成です")









