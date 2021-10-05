import sys
#sys.stdin=open("input.txt","rt")
N,K=map(int,input().split())
nums=list(map(int,input().split()))

res=set()
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum=nums[i]+nums[k]+nums[ j]
            res.add(sum)
res=list(res)
res.sort(reverse=True)
print(res[K-1])


