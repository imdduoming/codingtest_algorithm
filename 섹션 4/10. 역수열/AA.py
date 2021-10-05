import sys

#sys.stdin=open("input.txt","rt")
N=int(input())
a=list(map(int,input().split()))
seq=[0]*(N)
for i in range(N):
    for j in range(N):#seq 탐색
        if a[i]==0 and seq[j]==0:
            #자기앞에 자기보다 큰 숫자 갯수 확보 , 근데 seq 자리는 비어있는 상태 , 즉 자리차지
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x,end=' ')

