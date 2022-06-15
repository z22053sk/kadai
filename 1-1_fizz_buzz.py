#課題1-1: fizz_buzz.py
def fb(i):

    a = [[i%15,"FizzBuzz"],[i%5,"Buzz"],[i%3,"Fizz"],[0,""]] #余りを計算し、それぞれリストに代入する（15,5,3で割れる数値、配列4つ目は強制的に0で値無し） 
    a.sort(reverse=False,key=lambda x:x[0])                  #最小値をソートする (「0」であれば割り切れる。割り切れていない場合は値無し"空"）
    ret = a[:][0][1]                                         #最小値を抽出する、文字列のみを取り出す → ret = ret[1]  #文字のみを抽出する　[[0],"※"] 
    return ret

i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1
