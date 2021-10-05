import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int,input().split())
result=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        sum=i+j
        result.append(sum)
min_count=0
ans=[]
for a in range(2,N+M+1):
    if min_count<result.count(a):
        min_count=result.count(a)
        ans=[]
        ans.append(a)
    elif min_count==result.count(a):
        ans.append(a)

for i in ans:
    print(i,end=' ')
print()



