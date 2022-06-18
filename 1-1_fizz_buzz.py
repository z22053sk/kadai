#課題1-1: fizz_buzz.py
def fb(i):

    a = [[i%15,"FizzBuzz"],[i%5,"Buzz"],[i%3,"Fizz"],[0,""]]
    a.sort(reverse = False, key = lambda x:x[0])             
    ret = a[:][0][1]
    return ret

i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1
