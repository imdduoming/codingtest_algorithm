import sys
#sys.stdin=open("input.txt","rt")

a=[]
def check(arr):
    while len(arr)>1:
        if arr.pop()!=arr.pop(0):
            return False
    return True

cnt=0
for i in range(7):
    arr=list(map(int,input().split()))
    a.append(arr)
#열마다 행검사
for i in range(7):
    for j in range(0,3):
        check_arr=a[i][j:j+5:]
        #print(check_arr)
        if check(check_arr):
            cnt+=1
#행마다 열검사
for i in range(7):
    for j in range(0,3):
        check_arr=[]
        for k in range(j,j+5):
            check_arr.append(a[k][i])
            #print(check_arr)
        if check(check_arr):
            cnt+=1
print(cnt)