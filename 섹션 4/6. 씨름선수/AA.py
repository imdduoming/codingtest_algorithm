import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
men=[]
for i in range(N):
    height,weight=map(int,input().split())
    men.append((height,weight))
men.sort(key=lambda x:(x[0],x[1]))
cnt=N
for i in range(0,len(men)-1):
    tall=men[i][0]
    weight=men[i][1]
    for j in range(i+1,len(men)):
        if tall<=men[j][0] and weight<=men[j][1]:
            cnt-=1
            break

print(cnt)
