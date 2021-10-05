import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
def test(str):
    str=str.lower()
    word=[]
    for i in str:
        word.append(i)

    while len(word)>1:
        if word.pop(0)!=word.pop():
            return False
    return True
for i in range(1,N+1):
    word=input()
    if test(word):
        print('#%d YES' %i)
    else:
        print('#%d NO' % i)





