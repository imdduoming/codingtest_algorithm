import sys
#sys.stdin=open("input.txt","rt")
N,C=map(int,input().split())
magoogan=[]
for i in range(N):
    magoogan.append(int(input()))
magoogan.sort()
lt=min(magoogan)
rt=max(magoogan)
def arrange(mid):
    cnt=1
    start=magoogan[0]
    for i in range(1,len(magoogan)):
        if magoogan[i]-start<mid:
            continue
        else:
            start=magoogan[i]
            cnt+=1

            if cnt==C:
                return True
    return False

ans=0
while lt<=rt:
    mid=(lt+rt)//2
    if arrange(mid):
        ans=max(ans,mid)
        lt=mid+1
    else:
        rt=mid-1

print(ans)