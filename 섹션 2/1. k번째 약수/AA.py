import sys
#sys.stdin=open("input.txt","rt")
N,K=map(int,input().split())
cnt=0
k_is=0
for  i in range(1,N+1):
    if N%i==0:
        cnt+=1
    if cnt==K:
        k_is=1
        print(i)
        break
if k_is==0:
    print(-1)

