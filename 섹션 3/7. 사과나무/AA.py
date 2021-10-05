import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
farms=[]
for i in range(N):
    row=list(map(int,input().split()))
    farms.append(row)
cnt=0
mid=N//2
#print(mid)
for i in range(0,N):
    start=0
    end=0
    for j in range(0,N):
        if abs(mid-i)==j:
            start=j
            end=N-1-start
            cnt+=farms[i][j]
            #print('i:', i, 'j:', j, 'cnt:', cnt)
            if i==0 or i==N-1:
                break

        elif (start+j)//2==mid:
            end=j
            cnt += farms[i][j]
            #print('i:', i, 'j:', j, 'cnt:', cnt)
            break
        elif start<j and j<end:
            cnt+=farms[i][j]
            #print('i:', i, 'j:', j, 'cnt:', cnt)


print(cnt)