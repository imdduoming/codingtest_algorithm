import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
scores=[]
for i in range(N):
    nums=list(map(int,input().split()))
    scores.append(nums)
max_money=0
for score in scores:
    a,b,c=score[0],score[1],score[2]
    if a==b and b==c:
        money=10000+score[0]*1000
    elif a==b and a==c:
        money=1000+a*100
    elif b==c:
        money = 1000 + a * 100
    else:
        money=max(a,b,c)*100
    max_money=max(max_money,money)
print(max_money)





