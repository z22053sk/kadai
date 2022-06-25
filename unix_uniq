#課題2-3
import sys

#出力用の配列を準備
list = []  

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("wc: No such file or directory,"+ sys.argv[1])
else:
    sys.exit("usage: wc [file]")

line = f.readlines()
#重複が無い場合リストに追加する
for data in line:
    #読込ファイルの表示
    print(data)
    if line not in list: 
    list.append(line)

f.close()

#削除後データの表示
print('-----削除後データ----')
for item in list:
    print(item)
