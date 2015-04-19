
for i in range(9,0,-1):
    for k in range(i-1,1):
        print(end="    ")
    for j in range(9,0,-1):
        q=str.format("{0:1}*{1:1}={2:>2}",i,j,i*j)
        print(q,end="  ")
    print()
