n,m = map(int,input().split())
j = int(input())

s=0
q = [1,m] 
for v in range(0,j):
    app_koc = int(input())
    if q[0] <= app_koc and app_koc <= q[1]:
        continue
    else:
        right = app_koc - q[1]
        left = q[0] - app_koc
        s+=max(left,right)
        if left<right:
            q = [q[0]+right,app_koc]
        else:
            q = [app_koc,q[1]-left]
print(s)
#DP의 반례도 충분히 생각해야한다고 생각함