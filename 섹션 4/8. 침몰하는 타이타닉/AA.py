import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int,input().split())
weight=list(map(int,input().split()))
lt=0
rt=N-1
cnt=0
weight.sort()
while lt<=rt:
    if weight[lt]+weight[rt]>M:
        cnt+=1
        rt-=1
    elif weight[lt]+weight[rt]<=M:
        lt+=1
        rt-=1
        cnt+=1
    #print(weight[lt],weight[rt],cnt)
print(cnt)