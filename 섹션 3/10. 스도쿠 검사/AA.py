import sys
#sys.stdin=open("input.txt","rt")

nums=[]
def check(nums):
    #행
    for arr in nums:
        check={}
        for i in arr:
            if i not in check:
                check[i]=1
            else:
                return False
    #열검사
    for j in range(0,9):
        check={}
        for i in range(9):
            if nums[i][j] not in check:
                check[nums[i][j]]=1
            else:
                return False

    #3*3 박스 검사
    for k in range(0,9,3):
        check={}
        for i in range(0,3):
            for j in range(0,3):
                if nums[i][j] not in check:
                    check[nums[i][j]] = 1
                else:
                    return False
    return True





for i in range(9):
    arr=list(map(int,input().split()))
    nums.append(arr)

if check(nums):
    print("YES")
else:
    print("NO")