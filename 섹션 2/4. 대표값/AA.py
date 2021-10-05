import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
score=list(map(int,input().split()))
total=sum(score)
avg=round(float(total /N))
resMin=float('inf')
sel=[]
avg_abs=[]
for i in range(0,len(score)):
    avg_abs.append(abs(avg-score[i]))
Minabs=min(avg_abs)
for i in range(0,len(avg_abs)):
    if Minabs==avg_abs[i]:
        sel.append(i+1)

if len(sel)==1:
    print(avg,sel[-1])
elif len(sel)==2:
    if score[sel[0]-1]<score[sel[1]-1]:
        print(avg, sel[1])
    else:
        print(avg, sel[0])
else:
    print(avg,sel[0])





