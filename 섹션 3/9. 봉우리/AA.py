import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
a=[]
for i in range(N):
    arr=list(map(int,input().split()))
    a.append(arr)
a.insert(0,[0]*N)
a.append([0]*N)
for i in a:
    i.insert(0,0)
    i.append(0)

cnt=0


for i in range(1,N+1):
    for j in range(1,N+1):
        now=a[i][j]
        up=a[i-1][j]
        down=a[i+1][j]
        left=a[i][j-1]
        right=a[i][j+1]
        if now>up and now>down and now>left and now>right:
            cnt+=1



print(cnt)