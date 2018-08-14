# 変数定義部
cur_pos = 0 # 現在の位置

# 以下メイン処理
# 本来このコードは1行目と重複するため必要ないが、後の問題のため記述
cur_pos = 0

#dice_numに1を代入してください。(サイコロで出た目を代入する目的で後々使います)
dice_num = 1

#「(dice_num)の目が出ました。」の形式でサイコロの出た目を表示してください。
dice_magic = '{0}の目が出ました。'.format(dice_num)
print(dice_magic)

#cur_posの値にdice_numの値を足した結果をcur_posに再度代入してください。(サイコロの目だけ前に進む処理です。)
cur_pos = cur_pos + dice_num

#現在位置は(cur_pos)です。」の形式で現在位置を表示してください。
genzai_iti = '現在位置は{0}です。'.format(cur_pos)
print(genzai_iti)
