import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int,input().split())
video=list(map(int,input().split()))
lt=1
rt=sum(video)
min_ans=rt
def possible(mid):
    total=0
    cnt=1
    for i in video:
        total += i
        if total>mid:
            total=i
            cnt+=1

        #print('total:',total,'cnt:',cnt)

    if cnt>M:
        #print('mid:',mid,cnt)
        return False
    else:
        #print('mid:', mid, cnt)
        return True

while lt<=rt:
    mid=(lt+rt)//2
    #print('lt:',lt,'rt:',rt,'min_ans:',min_ans)
    if possible(mid):
        min_ans=min(min_ans,mid)
        rt=mid-1
    else:
        lt=mid+1
print(min_ans)
