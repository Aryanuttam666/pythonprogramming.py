n = int(input("rows: "))
for i in range(1,n+1):
    print(" "*(n-i),'*'*(2*i-1)," "*(n-i))

for i in range(n,0,-1):
    print(" "*(n-i),'*'*(2*i-1)," "*(n-i))
