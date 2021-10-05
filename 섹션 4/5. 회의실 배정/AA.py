import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
sche=[]
for i in range(N):
    start,end=map(int,input().split())
    sche.append((start,end))
sche.sort(key=lambda x:(x[1],x[0]))


start=0
cnt=0

for i in sche:
    if i[0]>=start:
        cnt+=1
        start=i[1]


print(cnt)




