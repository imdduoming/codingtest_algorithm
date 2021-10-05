import sys

#sys.stdin=open("input.txt","rt")
N=int(input())
nums=list(map(int,input().split()))

lt=0
rt=N-1
cnt=0
last=0
ans=''
tmp=[]
while lt<=rt:
    if nums[lt]>last:
        tmp.append((nums[lt],'L'))
    if nums[rt]>last:
        tmp.append((nums[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        ans+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(ans))
print(ans)


