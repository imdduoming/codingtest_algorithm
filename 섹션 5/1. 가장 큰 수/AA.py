import sys

#sys.stdin=open("input.txt","rt")
N,M=map(int,input().split())
N=list(str(N))
N=[int(x) for x in N]
lenN=len(N)
result_len=lenN-M
cnt=0
i=0
new_arr=[]
while i<=len(N)-1:

    #print(N[i])
    if not new_arr:
        new_arr.append(N[i])
        i+=1
        #print(new_arr, cnt)
    else:
        if new_arr[-1]>=N[i]:
            new_arr.append(N[i])
            i+=1


        else:
            flag=0
            while new_arr[-1]<N[i]:
                new_arr.pop()
                cnt+=1
                if cnt==M:
                    break
                if not new_arr:
                    break
            new_arr.append(N[i])
            i+=1
        #print(new_arr, cnt)
    if cnt == M:
        break
if len(new_arr)>result_len:
    for i in range(len(new_arr)-result_len):
        new_arr.pop()
elif len(new_arr)<result_len:
    for j in range(i,lenN):
        new_arr.append(N[j])


for i in new_arr:
    print(i,end='')










cnt=0

