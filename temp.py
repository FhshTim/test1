def C(n,r):
    if r == 1:
        return n
    elif n == r:
        return 1
    else:
        return C(n-1,r)+C(n-1,r-1)

   
def check(n,r):
    ans = []
    for i in range(1,n+1):
        ans.append(i)
    for j in range(1,r):
        for i in range(1,n):
            ans[i] = ans[i]+ans[i-1]
    
    return(ans[n-r])
    
def yanghui(n):
    q = []
    for _ in range(n):
        for _ in range(len(q)-1):
            q.append(q.pop(0)+q[0])
        q.append(1)
        print(q)
    
    
#yanghui(10)
print(check(990,33))
