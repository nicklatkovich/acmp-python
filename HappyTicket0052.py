n=list(map(int,list(input())))
print('YES'if sum(n[:3])==sum(n[3:])else'NO')