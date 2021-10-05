import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
farms=[]
for i in range(N):
    arr=list(map(int,input().split()))
    farms.append(arr)
M=int(input())
for i in range(M):
    h,t,k=map(int,input().split())
    if t==0:#왼쪽방향으로 회전
        for _ in range(k):
            farms[h-1].append(farms[h-1].pop(0))
    elif t==1:
        for _ in range(k):
            farms[h - 1].insert(0,farms[h - 1].pop())

start=0
end=N-1
cnt=0
for i in range(0,N):

    for j in range(start,end+1):
        cnt+=farms[i][j]
    if i<N//2:#모래시계이므로 좁혀들어감
        start+=1
        end-=1
    else:
        start-=1
        end+=1
print(cnt)

