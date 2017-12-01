e='2.71828182845904523536028750'
n=int(input())
print(3 if n==0 else e[:n+1]+chr(ord(e[n+1])+(1 if e[n+2]>'4'else 0)))